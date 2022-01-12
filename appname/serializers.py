from django.db import models
from .models import Employee
from rest_framework import fields, serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
        
