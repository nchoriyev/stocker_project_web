from django.shortcuts import render, redirect
from django.views import View
import requests



class Token:
    @staticmethod
    def token(username, password):
        url = "http://127.0.0.1:8000/api/token/"
        data = {
            "username": username,
            "password": password
        }

        response = requests.post(url, data=data)

        if response.status_code == 200:
            tokens = response.json()
            access_token = tokens.get("access")
            return access_token
        else:
            print("no token:", response.status_code, response.text)
            return None


class ServicesView(View):
    def get(self, request):
        token = Token.token('admin', '1234')

        headers = {
            "Authorization": f"Bearer {token}",
        }

        query = request.GET.get('search', '')

        api_url = f"http://127.0.0.1:8000/api/services-web/"
        if query:
            api_url += f"?search={query}"

        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            services = response.json()
        else:
            services = []

        context = {
            'services': services,
            'value': query
        }
        return render(request, 'service.html', context)


class HomeView(View):
    def get(self, request):
        token = Token.token('admin', '1234')

        headers = {
            "Authorization": f"Bearer {token}",
        }

        response = requests.get(f"http://127.0.0.1:8000/api/services-web/", headers=headers)

        if response.status_code == 200:
            datas = response.json()
            context = {"datas": datas}
        else:
            context = {"error": "Error!!"}

        return render(request, 'index.html', context)


class AboutView(View):
    def get(self, request):
        token = Token.token('admin', '1234')

        headers = {
            "Authorization": f"Bearer {token}",
        }

        response = requests.get("http://127.0.0.1:8000/api/abouts-web/", headers=headers)

        if response.status_code == 200:
            abouts = response.json()
            context = {"abouts": abouts}
        else:
            context = {"error": "error"}

        return render(request, 'about.html', context)


class BlogView(View):
    def get(self, request):
        token = Token.token('admin', '1234')

        headers = {
            "Authorization": f"Bearer {token}",
        }

        response = requests.get("http://127.0.0.1:8000/api/blogs-web/", headers=headers)

        if response.status_code == 200:
            blogs = response.json()
            context = {"blogs": blogs}
        else:
            context = {"error": "error!!"}

        return render(request, 'blog.html', context)


class ContactView(View):
    def get(self, request):
        token = Token.token('admin', '1234')

        headers = {
            "Authorization": f"Bearer {token}",
        }

        response = requests.get("http://127.0.0.1:8000/api/applications-web/", headers=headers)

        if response.status_code == 200:
            contacts = response.json()
            context = {"contacts": contacts}
        else:
            context = {"error": "Error!"}

        return render(request, 'contact.html', context)


class TeamView(View):
    def get(self, request):
        token = Token.token('admin', '1234')

        headers = {
            "Authorization": f"Bearer {token}",
        }

        response = requests.get("http://127.0.0.1:8000/api/staffs-web/", headers=headers)

        if response.status_code == 200:
            staffs = response.json()
            context = {"staffs": staffs}
        else:
            context = {"error": "Error!"}

        return render(request, 'team.html', context)

