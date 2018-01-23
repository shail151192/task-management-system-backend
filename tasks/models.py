from __future__ import unicode_literals

from django.db import models

#Create your models here.
class Task(models.Model):
    name=models.CharField(max_length=255, unique=True)
    description=models.TextField()
    status=models.CharField(max_length=255)
    deadline=models.DateTimeField(null=True)
    created_by=models.CharField(max_length=255, null=True)
    updated_by=models.CharField(max_length=255, null=True)
    created_on=models.DateTimeField(auto_now_add=True, null=True)
    updated_on=models.DateTimeField(auto_now=True, null=True)


    @staticmethod
    def create_task(data):
        data['status']='new'
        task=Task(name=data['name'], description=data['description'], status=data['status'], created_by=data['created_by'])
        task.save()
        return task

    def delete_task(self):
        self.delete()


    def update_task(self, data):
        print data
        self.name=data['name']
        self.description=data['description']
        self.updated_by=data['updated_by']
        self.save()





