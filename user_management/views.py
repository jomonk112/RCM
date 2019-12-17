from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .forms import UserForm

from mixins import ResponseViewMixin
from user_management.models import AppUser as User

from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import ObtainJSONWebToken

jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER

 
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


class UserLogin(APIView,ResponseViewMixin):
    authentication_classes = ()
    permission_classes = ()
    
    def post(self, request):
        jwt_token = ObtainJSONWebToken.as_view()(self.request._request)
        if jwt_token.status_code == status.HTTP_200_OK:
            token = jwt_token.data['token']
            payload = jwt_decode_handler(token)
            info = self.get_user_info(payload)
            data = {"token": token,
                    "token_expiry": payload['exp'],
                    "info": info}
            return self.rcm_response(code='HTTP_200_OK', data=data)
       
        return self.pd_error_response(code='HTTP_400_BAD_REQUEST', data=jwt_token.data['non_field_errors'])
    
    def get_user_info(self, payload):
        info = {"user_id": payload['user_id'],
                "email": payload['email'],
                "username": payload['username']}
        return info



