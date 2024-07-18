from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from .serializers import StudentSerializers
from class.models import Class
from .serializers import  ClassSerializer
from classperiod.models import ClassPeriod
from .serializers import ClassPeriodSerializer
from course.models import Course
from .serializers import CoursesSerializer
from teacher.models import Teacher
from .serializers import TeacherSerializer
from rest_framework import status

class StudentListView (APIView):
    def get (self,request):
        students = Student.objects.all()
        serializer = StudentSerializers(students,many = True)

        return Response(serializer.data)

class ClassesListView(APIView):
    def get(self,  request):
        Classes = Classes.objects.all()
        serializer = ClassesSerializer(Students, many=True)
        return Response(serializer.data)

class ClassPeriodListView(APIView):
    def get(self, request):
        ClassPeriod = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(ClassPeriod, many = True)
        return Response(serializer.data)

class CoursesListView(APIView):
    def get(self, request):
        Courses = Courses.objects.all()
        serializer = CoursesSerializer(Courses, many = True)
        return Response(serializer.data)
