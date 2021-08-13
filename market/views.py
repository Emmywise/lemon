from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderSerializer
# Create your views here.

class Order(APIView):

    def post(self, request): # post request for market order
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 