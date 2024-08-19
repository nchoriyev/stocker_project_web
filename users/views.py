from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from web.views import Token
import requests


def success_view(request):
    return render(request, 'success.html')


def login_view(request, ):
    if request.method == 'POST':
        # username = request.POST['username']
        # password = request.POST['password']
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('home')
        else:
            context = {"message": "Login yoki password xato!"}
            return render(request, 'auth/login.html', context)

    return render(request, "auth/login.html")


def register_view(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password1')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username Allaqachon mavjud.")
            return render(request, "auth/register.html")

        # Check if passwords match
        if password != password2:
            messages.error(request, "Password bir xil emas.")
            return render(request, "auth/register.html")

        try:
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name,
                                            last_name=last_name)
            user.save()
            messages.success(request, "Registratsiya qilindi! Xush kelibsiz")
            return redirect('login')
        except ValidationError as e:
            messages.error(request, f"Error: {e}")
            return render(request, "auth/register.html")
        except Exception as e:
            messages.error(request, f"Error: {e}")
            return render(request, "auth/register.html")

    return render(request, "auth/register.html")


def logout_view(request):
    logout(request)
    return redirect('home')


def show_user(request):
    if request.user.is_authenticated:
        user = request.user
        context = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'email': user.email
        }
        return render(request, 'show_user.html', context)
    else:
        return redirect('login')




@login_required(login_url='auth/login')
def service_detail(self, request, id):
    token = Token.token('admin', '1234')

    headers = {
        "Authorization": f"Bearer {token}",
    }

    response = requests.get(f"http://127.0.0.1:8000/api/services-web/{id}", headers=headers)

    if response.status_code == 200:
        service = response.json()
        context = {"servic": service}
    else:
        context = {"error": "Error!!"}

    return render(request, 'service_detail.html', context)
