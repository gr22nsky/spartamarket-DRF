from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns = [
    path('', views.SignUpView.as_view()),
    path('login/', views.LogInView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view()),
    path('logout/', views.LogOutView.as_view()),
    path('<str:username>/', views.ProfileView.as_view()),
]
