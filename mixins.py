import json
from django.conf import settings

from rest_framework.response import Response
from rest_framework import status





class ResponseViewMixin(object):
    ignore_keys = ['non_field_errors']

    def rcm_response(self, code='HTTP_200_OK', data=None):
        return Response(
            headers={'status': getattr(status, code)},
            status=getattr(status, code),
            data={
                'status': getattr(status, code),
                'data': data
            },
            content_type='application/json'
        )

    def rcm_error_response(self, code='HTTP_500_INTERNAL_SERVER_ERROR', data=None):

        return Response(
            headers={'status': getattr(status, code)},
            status=getattr(status, code),
            data={
                'status': getattr(status, code),
                'error': data
            },
            content_type='application/json'
        )

    def rcm_exception_response(self, e_code):
        msg = "The server responded with " + e_code.lower() + " status"

        return self.pd_error_response('HTTP_500_INTERNAL_SERVER_ERROR', msg)
    
    def get_form_errors_if_any(self,form):
        """
        Process form errors to required format
        """
        form_data = [(k, v[0]) for k, v in form.errors.items()]
        validations = [{'field': key, 'error_message': value} for key, value in form_data]

        return validations


