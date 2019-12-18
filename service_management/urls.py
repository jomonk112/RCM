from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .views import BrandManagement,CouponManagement


router = DefaultRouter()

router.register(r'brand', BrandManagement, basename='brands')
router.register(r'coupon', CouponManagement, basename='coupons')

urlpatterns = [
    path('', include(router.urls)),
]