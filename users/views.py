from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from users.models import AuthUser
from users.serializer import UserSerializer
# Create your views here.

class User(APIView):
    def post(self, request):
        res = AuthUser.create_user(request.data)
        return Response(data={'message': 'user successfully created', 'success':True}, status=status.HTTP_200_OK )




@api_view(http_method_names=['POST'])
def user_login(request):
    try:
        token, user=AuthUser.authenticate_user(request.data['username'], request.data['password'])
        print user
        # serializer=UserSerializer(user)
        return Response(data={'data': {'token': token, 'user':user}, 'success': True}, status=status.HTTP_200_OK)

    except Exception as err:
        return Response(data={'message': err.message, 'success': False}, status=status.HTTP_400_BAD_REQUEST)