# myapp/urls.py
from django.urls import path
from .views import login_view, user_dashboard, CompareProfilesView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name='sign-in'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('compare-profiles/', CompareProfilesView.as_view(), name='compare-profiles'),
    path('dashboard/', user_dashboard, name='dashboard'),
]