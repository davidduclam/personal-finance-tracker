from django.http import JsonResponse
from .models import Income, Expense
from .serializers import IncomeSerializer, ExpenseSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

'''
Endpoints for Income
'''

@api_view(['GET', 'POST'])
def income_list(request, format = None):

    if request.method == 'GET':
        incomes = Income.objects.all()
        serializer = IncomeSerializer(incomes, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = IncomeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def income_detail(request, id, format = None):

    try:
        income = Income.objects.get(pk=id)
    except Income.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IncomeSerializer(income)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = IncomeSerializer(income, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        income.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


'''
Endpoints for Expense
'''

@api_view(['GET', 'POST'])
def expense_list(request, format = None):

    if request.method == 'GET':
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ExpenseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def expense_detail(request, id, format = None):

    try:
        expense = Expense.objects.get(pk=id)
    except Expense.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ExpenseSerializer(expense, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)