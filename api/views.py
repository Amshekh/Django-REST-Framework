from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company, Employee
from api.serializers import Company_Serializer, Employee_Serializer
from rest_framework.decorators import action
from rest_framework.response import Response

class Company_ViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = Company_Serializer

    @action(detail=True, methods=['GET'])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emps_serializer = Employee_Serializer(emps, many=True, context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Error! Company does not exist'
            })


class Employee_ViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = Employee_Serializer