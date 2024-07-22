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

    def post(self, request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)    


class StudentDetailView(APIView):
    def get (self, request,id):
        student= Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)


    def put (self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)    



    def delete(self, request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status = status.HTTP_202_ACCEPTED)



class ClassListView(APIView):
    def get(self,  request):
        Class = Class.objects.all()
        serializer = ClassSerializer(Class, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = ClassSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)    



class ClassDetailView(APIView):
    def get (self, request,id):
        Class= Class.objects.get(id=id)
        serializer = ClassSerializer(student)
        return Response(serializer.data)


    def put (self, request, id):
        Class = Class.objects.get(id=id)
        serializer = ClassSerializer(Class, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)    



    def delete(self, request, id):
        Class = Class.objects.get(id=id)
        Class.delete()
        return Response(status = status.HTTP_202_ACCEPTED)


class ClassPeriodListView(APIView):
    def get(self, request):
        ClassPeriod = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(ClassPeriod, many = True)
        return Response(serializer.data)

     def post(self, request):
        serializer = ClassPeriodSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)    


class ClassPeriodDetailView(APIView):
    def get (self, request,id):
        ClassPeriod= ClassPeriod.objects.get(id=id)
        serializer = ClassSerializer(classperiod)
        return Response(serializer.data)


    def put (self, request, id):
        ClassPeriod = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(ClassPeriod, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)    



    def delete(self, request, id):
        ClassPeriod = ClassPeriod.objects.get(id=id)
        ClassPeriod.delete()
        return Response(status = status.HTTP_202_ACCEPTED)

class CourseListView(APIView):
    def get(self, request):
        Course = Course.objects.all()
        serializer = CourseSerializer(Course, many = True)
        return Response(serializer.data)


     def post(self, request):
        serializer = CourseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)    


class CourseDetailView(APIView):
    def get (self, request,id):
        Course= Course.objects.get(id=id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)


    def put (self, request, id):
        Course= Course.objects.get(id=id)
        serializer = CoursePeriodSerializer(Course, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)    



    def delete(self, request, id):
        Course = Course.objects.get(id=id)
        Course.delete()
        return Response(status = status.HTTP_202_ACCEPTED)
