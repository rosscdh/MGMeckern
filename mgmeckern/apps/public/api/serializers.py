# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model

from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        exclude = ('username',
                   'password',
                   'user_permissions',
                   'groups',
                   'is_superuser',
                   'is_staff',
                   'is_active',)
