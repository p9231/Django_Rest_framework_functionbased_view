from django.shortcuts import render
from .models import Books
from .serializers import SerializerBooks
from rest_framework.response import Response
from rest_framework.views import APIView


class Books_list_View(APIView):
    
    def get(self, request):
        books = Books.objects.all()
        serializer = SerializerBooks(books, many= True)
        json = serializer.data
        return Response(json)
    
    def post(self, request):
        serializer = SerializerBooks(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)





