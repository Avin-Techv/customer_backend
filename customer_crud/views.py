from django.shortcuts import render

from rest_auth.registration.views import RegisterView

# Create your views here.

class CustomRegisterView(RegisterView):

    def get_response_data(self, user):
        return {'message': 'user registration success'}
