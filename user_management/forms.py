from django import forms
from .models import AppUser

class UserForm(forms.ModelForm):

    class Meta:
        model = AppUser
        fields = '__all__'

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        password = self.cleaned_data["password"]
        if password:
            user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user