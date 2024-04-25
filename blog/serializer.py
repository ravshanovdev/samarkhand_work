from rest_framework import serializers
from .models import MyResume, Variants, Test
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class MyResumeSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = MyResume
        fields = "__all__"


class VariantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variants
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'
