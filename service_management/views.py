from django.shortcuts import render

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from rest_framework import viewsets
from mixins import ResponseViewMixin
from .forms import BrandForm, CouponForm
from .models import Coupons
from .messages import *


class BrandManagement(viewsets.ViewSet, ResponseViewMixin):
    
    def create(self, request):
        data = request.data
        form = BrandForm(data, instance=None)
        if form.is_valid():
            brand = form.save()
            return self.rcm_response(code='HTTP_200_OK', data={"id": str(brand.id),
                                                              "message": BRAND_ADD})
        return self.rcm_error_response(code='HTTP_400_BAD_REQUEST', data=self.get_form_errors_if_any(form)[0])


class CouponManagement(viewsets.ViewSet, ResponseViewMixin):

    def create(self, request):
        data = request.data
        form = CouponForm(data, instance=None)
        if form.is_valid():
            coupon = form.save()
            return self.rcm_response(code='HTTP_200_OK', data={"id": str(coupon.id),
                                                              "message": COUPON_ADD})
        return self.rcm_error_response(code='HTTP_400_BAD_REQUEST', data=self.get_form_errors_if_any(form)[0])
    
    def update(self, request, pk):
        data = request.data
        coupon = Coupons.objects.get(id=pk)
        form = CouponForm(data, instance=coupon)
        if form.is_valid():
            coupon = form.save()
            return self.rcm_response(code='HTTP_200_OK', data={"id": str(coupon.id),
                                                              "message": COUPON_UPDATE})
        return self.rcm_error_response(code='HTTP_400_BAD_REQUEST', data=self.get_form_errors_if_any(form)[0])
    
    
    
    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_cookie)
    def list(self, request):
        amount = self.request.query_params.get('amount', None)
        brand = self.request.query_params.get('brand', None)

        coupons = Coupons.objects.all()
        
        if amount:
            coupons = coupons.filter(denomination=amount)
        if brand:
            coupons = coupons.filter(brand__brand_name=str(brand))
        
        results = [{'id':str(item.id),'brnad_name':item.brand.brand_name,
                    'brand_id':str(item.brand.id),
                    'coupon_code': item.coupon_code,
                    'amount':item.currency_code +" "+str(item.denomination)
                    }for item in coupons]
        return self.rcm_response(code='HTTP_200_OK', data={"results": results})
    
    
    
    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_cookie)
    def retrieve(self,request,pk):
        try:
            coupon = Coupons.objects.get(pk=pk)
            result = {'id':str(coupon.id),'brnad_name':coupon.brand.brand_name,
                        'brand_id':str(coupon.brand.id),
                        'coupon_code': coupon.coupon_code,
                        'amount':coupon.currency_code +" "+str(coupon.denomination)
                        }
            return self.rcm_response(code='HTTP_200_OK', data={"results": result})
        except Exception as e:
            return self.rcm_error_response(code='HTTP_400_BAD_REQUEST', data={'status':False,
                                                                              'message':str(e)})
            
        
            