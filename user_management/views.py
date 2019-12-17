from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .forms import UserForm


 






class UserSignup(viewsets.ViewSet):

    def create(self, request):
        data = request.data
        form = UserForm(data, instance=None)
        if form.is_valid():
            user = form.save()
            return Response(
                headers={'status': getattr(status, 'HTTP_200_OK')},
                status=getattr(status, 'HTTP_200_OK'),
                data={
                    'status': getattr(status, 'HTTP_200_OK'),
                    'data': data
                },
                content_type='application/json'
            )

class UserLogin(APIView):

    def post(self, request):
        pass

