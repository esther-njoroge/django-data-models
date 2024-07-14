from rest_framework import serializers
from student.models import student

class StudentSerializers(serializers.modelserializer):
    class meta:
        model = student
        fields = "__all__"