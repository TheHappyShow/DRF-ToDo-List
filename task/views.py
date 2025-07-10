from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsOwner

from .models import Task
from .serializers import TaskSerializer
# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = (IsOwner, )

    def get_queryset(self):
        user = self.request.user.id
        return Task.objects.filter(user_id=user)