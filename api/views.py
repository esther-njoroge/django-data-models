from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIview
from student.models import Student
from serializers import StudentSerializers

class StudentListView (APIview):
    def get (self,request):
        students = Student.objects.all()
        serializer = StudentSerializers(students,many = True)

        return Response(serializer.data)