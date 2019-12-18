from django.shortcuts import render

from rest_framework import viewsets
from mixins import ResponseViewMixin
from .forms import BrandForm, CouponForm


class BrandManagement(viewsets.ViewSet, ResponseViewMixin):
    
    def create(self, request):
        data = request.data
        form = BrandForm(data, instance=None)
        if form.is_valid():
            brand = form.save()
            return self.rcm_response(code='HTTP_200_OK', data={"id": str(brand.id),
                                                              "message": "Brand added successfully"})
        return self.rcm_error_response(code='HTTP_400_BAD_REQUEST', data=self.get_form_errors_if_any(form)[0])


class CouponManagement(viewsets.ViewSet, ResponseViewMixin):

    def create(self, request):
        print("hit in coupon")
        data = request.data
        form = CouponForm(data, instance=None)
        if form.is_valid():
            coupon = form.save()
            return self.rcm_response(code='HTTP_200_OK', data={"id": str(coupon.id),
                                                              "message": "Coupon added successfully"})
        return self.rcm_error_response(code='HTTP_400_BAD_REQUEST', data=self.get_form_errors_if_any(form)[0])
            
