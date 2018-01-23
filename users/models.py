from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings
import jwt
from django.conf import settings
from django.contrib.sessions.models import Session

class AuthUser(User):

    @staticmethod
    def create_user(data):
        data['is_active']=True
        user = User.objects.create_user(**data)
        user.save()
        return user

    @staticmethod
    def authenticate_user(username, password):
        payload_handler=api_settings.JWT_PAYLOAD_HANDLER
        encode_handler=api_settings.JWT_ENCODE_HANDLER

        try:
            user = authenticate(username=username, password=password)
            if user is not None:
                import datetime
                payload ={'username':username, 'password': password}
                token = {jwt.encode(payload, settings.SECRET_KEY)}
                s=Session(session_key=username, session_data=payload, expire_date=datetime.datetime(2018, 4, 20, 13, 35, 12))
                s.save()
                return token, username
            else:
                raise Exception('Invalid username or password')

        except Exception as err:
            raise Exception(err.message)

