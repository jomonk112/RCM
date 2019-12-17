from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .forms import UserForm

from mixins import ResponseViewMixin


 
class UserSignup(viewsets.ViewSet,ResponseViewMixin):
    authentication_classes = ()
    permission_classes = ()

    def create(self, request):
        data = request.data
        form = UserForm(data, instance=None)
        if form.is_valid():
            user = form.save()
            return self.rcm_response(code='HTTP_200_OK', data={"id": str(user.id),
                                                              "message": "Record added successfully"})
        return self.rcm_error_response(code='HTTP_400_BAD_REQUEST', data=self.get_form_errors_if_any(form)[0])


class UserLogin(APIView):

    def post(self, request):
        pass

