from django import forms
from .models import Brands

class BrandForm(forms.ModelForm):

    class Meta:
        model = Brands
        fields = '__all__'