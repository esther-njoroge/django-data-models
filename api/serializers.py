from rest_framework import serializers
from student.models import Student
from class.models import Class
from classperiod.models import ClassPeriod
from course.models import Course
from teacher.models import Teacher

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = "__all__"
class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = "__all__"
class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"