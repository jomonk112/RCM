from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .views import UserLogin,UserSignup

urlpatterns = [
    path('login',UserLogin.as_view())
]
router = DefaultRouter()
router.register(r'signup', UserSignup, basename='signup')
urlpatterns = urlpatterns + router.urls