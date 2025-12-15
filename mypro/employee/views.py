from django.http import Http404
from django.shortcuts import render
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from employee.models import Employee
from rest_framework.response import Response
from employee.serializers import EmployeeSerializer
from rest_framework.views import APIView


#Function-based:-

# API view for reading all employee records from table
# @api_view(['GET','POST'])
# def employeelist(request):#non primary key based
#     #for reading all employee records from employee table.
#     if request.method == 'GET':
#         e = Employee.objects.all()
#         emp=EmployeeSerializer(e, many=True)
#         return Response(emp.data,status=status.HTTP_200_OK)#sends response back to client side
#     #for creating new employee records.
#     if request.method == 'POST':
#         e = EmployeeSerializer(data=request.data)
#         if e.is_valid():
#             e.save()
#             return Response(e.data, status=status.HTTP_201_CREATED)

# @api_view(['GET','PUT','DELETE'])
# def employeedetails(request,pk):
#     try:
#         e = Employee.objects.get(pk=pk)
#     except:
#         return Response({"message": "employee not found"}, status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         emp=EmployeeSerializer(e)
#         return Response(emp.data,status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         emp = EmployeeSerializer(e, data=request.data)
#         if emp.is_valid():
#             emp.save()
#             return Response(emp.data, status=status.HTTP_201_CREATED)
#     elif request.method == 'DELETE':
#         e.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#class-based
#
# class EmployeeList(APIView):
#     def get(self, request):
#         e=Employee.objects.all()
#         emp=EmployeeSerializer(e,many=True)
#         return Response(emp.data,status=status.HTTP_200_OK)
#     def post(self,request):
#         emp=EmployeeSerializer(data=request.data)
#         if emp.is_valid():
#             emp.save()
#             return Response(emp.data,status=status.HTTP_201_CREATED)
#
# class EmployeeDetail(APIView):
#     def get_object(self,pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except:
#             raise Http404
#     def get(self, request, pk):
#         e = self.get_object(pk)
#         emp = EmployeeSerializer(e)
#         return Response(emp.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         e = self.get_object(pk)
#         emp = EmployeeSerializer(e, data=request.data)
#         if emp.is_valid():
#             emp.save()
#             return Response(emp.data, status=status.HTTP_201_CREATED)
#
#
#
#     def delete(self, request, pk):
#         e = self.get_object(pk)
#         e.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#mixinview

class EmployeeList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def get(self, request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class EmployeeDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
