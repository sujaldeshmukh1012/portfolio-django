from django.shortcuts import render

# Create your views here.
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from .models import Courses, CourseIntrest
from .serializers import CoursesSerializer, CourseIntrestSerializer


class CourseList(APIView):
    def get(self, request, format=None):
        courses = Courses.objects.all()
        serializer = CoursesSerializer(courses, many=True)
        return Response(serializer.data)


class CourseDetails(APIView):
    def get(self, request, slug, format=None):
        course_detail = Courses.objects.filter(slug=slug)
        serializer = CoursesSerializer(course_detail, many=True)
        return Response(serializer.data)


class CourseIntrestView(APIView):
    def get(self, request, format=None):
        CourseIntrests = CourseIntrest.objects.all()
        serializer = CourseIntrestSerializer(CourseIntrests, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CourseIntrestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
