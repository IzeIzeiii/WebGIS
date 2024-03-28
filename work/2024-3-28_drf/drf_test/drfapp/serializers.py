from rest_framework import serializers

from .models import Course
from django.contrib.auth.models import User

# class CourseSerializer(serializers.HyperlinkedModelSerializer):
#     teacher=serializers.ReadOnlyField(source='teacher.username')
#     class Meta:
#         model=Course
#         fields=('name','introduction','teacher','price','url')
#         depth=2

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'
        depth=2

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'