from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tasks.models import *
from tasks.serializers import TaskSerializer
from tms.user_authentication import TokenAuthentication

# Create your views here.

class TaskListView(APIView):
    authentication_classes = (TokenAuthentication,)
    def post(self, request):
        try:
            data = request.data
            data['created_by']=request.current_user
            required_fields = ['name', 'description']
            fields=data.keys()
            missing_fields=list(set(required_fields)-set(fields))
            if missing_fields:
                return Response({'error': ",".join(missing_fields) + " is missing please provide it"})

            task=Task.create_task(data)
            serializer=TaskSerializer(task)
            return Response(data={'data': serializer.data, 'success':True},
                            status=status.HTTP_200_OK)
        except Exception as err:
            return Response(data={'message': err.message, 'success': False},
                            status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        tasks=Task.objects.all()
        serializer=TaskSerializer(tasks, many=True)
        return Response(data={'data': serializer.data, 'success': True},
                        status=status.HTTP_200_OK)

class TaskDetailView(APIView):
    authentication_classes = (TokenAuthentication,)
    def get(self, request, pk):
        try:
            task=Task.objects.get(id=pk)
            serializer = TaskSerializer(task)
            return Response(data={'data': serializer.data, 'success': True},
                        status=status.HTTP_200_OK)

        except Exception as err:
            return Response(data={'data': err.message, 'success': False},
                            status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            data=request.data
            print request.user
            data['updated_by']=request.current_user
            task = Task.objects.get(id=pk)
            task.update_task(data)
            return Response(data={'message': 'Task successfully updated', 'success': True},
                            status=status.HTTP_200_OK)
        except Exception as err:
            return Response(data={'message': err.message, 'success': False},
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = Task.objects.get(id=pk)
        task.delete_task()
        return Response(data={'message': 'Task successfully deleted', 'success': True},
                        status=status.HTTP_200_OK)






