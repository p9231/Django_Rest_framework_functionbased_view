from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Course
from .serializer import SerializerCourse


@api_view(["GET", "POST"])
def courseListView(request):
    if request.method == "GET":
        courses = Course.objects.all()
        courseserializer = SerializerCourse(courses, many=True)
        return Response(courseserializer.data)
    
    elif request.method == "POST":
        courseserializer = SerializerCourse(data = request.data)
        if courseserializer.is_valid():
            courseserializer.save()
            return Response(courseserializer.data, status=status.HTTP_201_CREATED)
        
        return Response(courseserializer.errors)
    

@api_view(['GET', 'PUT', 'DELETE'])    
def courseDetailView(request, pk):
    
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        courseserializer = SerializerCourse(course)
        return Response(courseserializer.data)
    
    elif request.method == 'PUT':
        courseserializer = SerializerCourse(course, data=request.data)
        if courseserializer.is_valid():
            courseserializer.save()
            return Response(courseserializer.data)
        
        return Response(courseserializer.errors)
    
    elif request.method == 'DELETE':
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
