from rest_framework import status, exceptions
from rest_framework.authentication import BaseAuthentication, get_authorization_header
import jwt
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

class TokenAuthentication(BaseAuthentication):

    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        if not auth or auth[0].lower() != b'token':
            msg = 'Invalid token header. No credentials provided.'
            raise exceptions.AuthenticationFailed(msg)

        if len(auth) == 1:
            msg = 'Invalid token header. No credentials provided.'
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = 'Invalid token header'
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1]
            if token == "null":
                msg = 'Null token not allowed'
                raise exceptions.AuthenticationFailed(msg)
        except UnicodeError:
            msg = 'Invalid token header. Token string should not contain invalid characters.'
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(request, token)

    def authenticate_credentials(self, request,token):
        payload = jwt.decode(token, settings.SECRET_KEY)
        username = payload['username']
        password = payload['password']
        msg = {'Error': "Token mismatch", 'status': "401"}
        try:
            user = User.objects.get(
                username=username,
                is_active=True
            )

        except jwt.ExpiredSignature or jwt.DecodeError or jwt.InvalidTokenError:
            msg="Invalid token"
            raise exceptions.AuthenticationFailed(msg)
        except User.DoesNotExist:
            msg="user does not exist"
            raise exceptions.AuthenticationFailed(msg)

        request.current_user=username
        request.token=token
        return (user, token)

    def authenticate_header(self, request):
        return 'Token'