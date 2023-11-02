from rest_framework.response import Response
from User.models import Task,User
from Admin.models import Apps,Admin
from .serializers import UserSerializer, TaskSerializer, AppsSerializer,AdminSerializer
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

class AdminList(APIView):
    def get(self,request):
        list = Admin.objects.all()
        serializer = AdminSerializer(list,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class UserList(APIView):
    def get(self,request):
        list = User.objects.all()
        serializer = UserSerializer(list,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class CreateAdmin(APIView):
    def post(self, request):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class CreateUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class CreateApp(APIView):
    def post(self, request):
        serializer = AppsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        

class AppList(APIView):
    def get(self,request):
        tasks = Apps.objects.all()
        serializer = AppsSerializer(tasks, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
class TaskCompletedByUser(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            completed_tasks = Task.objects.filter(user=user)
            serializer = TaskSerializer(completed_tasks, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"status": "error", "message": "User not found"}, status=status.HTTP_404_NOT_FOUND)


class TaskDetails(APIView):
    def get(self, request, id):
        try:
            task = Apps.objects.get(id=id)
            serializer = AppsSerializer(task)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Apps.DoesNotExist:
            return Response({"status": "error", "error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
