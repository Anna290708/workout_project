from django.urls import path
from .views import (
    RegisterPageView, LoginPageView,
    ProfilePageView, HistoryPageView, LogoutView
)

urlpatterns = [
    path('register-page/', RegisterPageView.as_view(), name='register'),
    path('login-page/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile-page/', ProfilePageView.as_view(), name='profile'),
    path('history-page/', HistoryPageView.as_view(), name='history'),
]
