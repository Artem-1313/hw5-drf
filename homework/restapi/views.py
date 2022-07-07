from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from django.views.generic import TemplateView
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT

from .serializer import my_name_Serializer, calculatorSerializer, StoreSerializer
from rest_framework import serializers
from rest_framework.views import APIView
from .models import Store


class menu(TemplateView):
    template_name = "restapi/menu.html"


class ListStore(APIView):
    def get(self, request, format=None):
        store = Store.objects.all()
        serializer = StoreSerializer(store, many=True)
        return Response(serializer.data)


class AddStore(APIView):
    def get(self, request):
        return Response({
            'name': 'write your name',
            'description': 'write your description',
            'rate': 4

        })

    def post(self, request):
        serializer = StoreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)


class StoreDetail(APIView):
    def get_object(self, pk):
        try:
            return Store.objects.get(pk=pk)
        except Store.DoesNotExist:
            raise serializers.ValidationError("No such store object")

    def get(self, request, pk):
        store = self.get_object(pk)
        serializer = StoreSerializer(store)
        return Response(serializer.data)

    def put(self, request, pk, format=None):

        store = self.get_object(pk)
        serializer = StoreSerializer(store, data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        store = self.get_object(pk)
        store.delete()
        return Response(status=HTTP_204_NO_CONTENT)


@api_view(['GET'])
def today(request):
    data = {
        "date": datetime.today().strftime('%d/%m/%Y'),
        "year": datetime.today().year,
        "month": datetime.today().month,
        "day": datetime.today().day
    }
    return Response(data)


@api_view(['GET'])
def hello_world(request):
    return Response({"msg": "Hello, World!"})


@api_view(['POST', 'GET'])
def my_name(request):
    if request.method == 'POST':
        serializer = my_name_Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    if request.method == "GET":
        return Response({"name": "name_of_hacker"})


@api_view(['POST', 'GET'])
def calculator(request):
    if request.method == 'GET':
        return Response({
            'action': "*",
            'number1': 1,
            'number2': 2
        })

    if request.method == "POST":
        serializer = calculatorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        calc = request.data

        if not isinstance(calc['number1'], int) or not isinstance(calc['number2'], int):
            raise serializers.ValidationError("Number1 and Number2 must be int")

        if calc['action'] == "+":
            var = calc['number1'] + calc['number2']
        elif calc['action'] == '-':
            var = calc['number1'] - calc['number2']
        elif calc['action'] == '/':
            var = calc['number1'] / calc['number2']
        elif calc['action'] == '*':
            var = calc['number1'] * calc['number2']
        return Response({"result": var})
    return Response([])
