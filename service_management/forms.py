from django import forms
from django.core.exceptions import ValidationError
from .models import Brands, Coupons

class BrandForm(forms.ModelForm):

    class Meta:
        model = Brands
        fields = '__all__'
        
class CouponForm(forms.ModelForm):
    
    class Meta:
        model = Coupons
        fields = '__all__'
    def clean(self):
        cleaned_data = super(CouponForm, self).clean()
        coupon = Coupons.objects.filter(coupon_code__iexact=cleaned_data['coupon_code']).exclude(id=self.instance.id)
        if coupon.exists():
            raise ValidationError("Coupon with this code exists")