from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ExpenseSerializer
from .models import Expense ,UserDetails
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


class ExpenseManagement(APIView):
    permission_classes =[IsAuthenticated ,TokenHasReadWriteScope]
    def get(self,request):
        serialized_data = ExpenseSerializer(Expense.objects.all() ,many=True).data
        return  Response(serialized_data ,status.HTTP_200_OK)
    
    def post(self,request):
        serialized_data = ExpenseSerializer(data = request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data , status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors ,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["GET"])
@permission_classes([IsAuthenticated ])
def filter_expense(request ,year , month):
    query_set = Expense.objects.filter(year = year ,month = month)
    serialized_data = ExpenseSerializer(query_set ,many=True).data
    return Response(serialized_data,status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated ])
def total_expense(request ,year , month):
    
    user_salary = UserDetails.objects.get(user= request.user
                                          ).monthly_salary
    total_expense = Expense.objects.filter(user= request.user,
                                           year=year ,month=month)
    if month is not None:
        total_expense = total_expense.filter(month = month)
    expense = total_expense.aggregate("amount")
    response ={
        "total_expense":expense ,"total_salary":user_salary,
        "remaining_amount":user_salary - expense
    }
    return Response(response ,status=status.HTTP_200_OK)
