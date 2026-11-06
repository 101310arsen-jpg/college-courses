from rest_framework import generics

from .models import Teacher, Course, Student
from .serializers import TeacherSerializer, CourseSerializer, StudentSerializer


class TeacherListView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.select_related('teacher').all()
    serializer_class = CourseSerializer


class StudentListView(generics.ListAPIView):
    queryset = Student.objects.prefetch_related('courses').all()
    serializer_class = StudentSerializer