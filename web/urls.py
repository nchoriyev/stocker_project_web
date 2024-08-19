from django.urls import path
from .views import HomeView, AboutView, ServicesView, BlogView, ContactView, TeamView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('services/', ServicesView.as_view(), name='service'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('team/', TeamView.as_view(), name='team'),
]