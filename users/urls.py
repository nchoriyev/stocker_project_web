from django.urls import path
from .views import login_view, register_view, logout_view, show_user, service_detail

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('show_user/', show_user, name='show_user'),
    path('<int:id>/service_detail', service_detail, name='service_detail'),
]