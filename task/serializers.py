from rest_framework import serializers
from .models import Task

# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = ('title', 'description')


class TaskSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = "__all__"


