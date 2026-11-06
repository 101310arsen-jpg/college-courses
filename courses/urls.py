from django.urls import path

from .views import TeacherListView, CourseListView, StudentListView


urlpatterns = [
    path('teachers/', TeacherListView.as_view(), name='teacher-list'),
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('students/', StudentListView.as_view(), name='student-list'),
]