from rest_framework import serializers
from api.models import Company, Employee

class Company_Serializer(serializers.HyperlinkedModelSerializer): # Advantage of HyperlinkedModelSerializer is i can define Meta class and in that i can tell what model i'm going to use.
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = "__all__"  # This will take all fields i have created in Company model

class Employee_Serializer(serializers.HyperlinkedModelSerializer):
    emp_id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = "__all__"