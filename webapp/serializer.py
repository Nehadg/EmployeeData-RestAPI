from rest_framework import serializers
from . models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        #fields = ('firstname','lastname')
        fields = '__all__'  #(__all__ return all databse list)