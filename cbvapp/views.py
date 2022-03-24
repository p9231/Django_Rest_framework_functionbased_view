from django.shortcuts import render
from .models import Books
from .serializers import SerializerBooks
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework  import status
from rest_framework import mixins, generics



class Books_list_View(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = SerializerBooks
    

class Books_details_view(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = SerializerBooks



"""
class Books_list_View(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    
    queryset = Books.objects.all()
    serializer_class = SerializerBooks
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class Books_details_view(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    
    queryset = Books.objects.all()
    serializer_class = SerializerBooks
    
    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)

"""

"""
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


class Books_details_view(APIView):
    
    def get_book(self, pk):
        try:
            return Books.objects.get(pk=pk)
        except Books.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        book = self.get_book(pk)
        serializer = SerializerBooks(book)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        book = self.get_book(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        book = self.get_book(pk)
        serializer = SerializerBooks(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)

"""