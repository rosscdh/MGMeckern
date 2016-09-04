# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model

from rest_framework import viewsets

from .serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = get_user_model().objects.all()
    serializer_class = AccountSerializer

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            return self.queryset.filter(pk=self.request.user.pk)
        else:
            return self.queryset.none()
