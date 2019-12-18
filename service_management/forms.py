from django import forms
from .models import Brands, Coupons

class BrandForm(forms.ModelForm):

    class Meta:
        model = Brands
        fields = '__all__'
        
class CouponForm(forms.ModelForm):
    
    class Meta:
        model = Coupons
        fields = '__all__'