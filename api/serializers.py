from rest_framework import serializers
from User.models import Task,User
from Admin.models import Apps,Admin

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class AppsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apps
        fields = '__all__'
