from django.urls import path
from .views import StudentListView, ClassListView, ClassPeriodListView, CourseListView, TeacherListView, StudentDetailView

urlpatterns = [
    path("students/", StudentListView.as_view(),name = "student_list_view"),
    path('course/', CourseListView.as_view(),name = 'course_list_view'),
    path('class/', ClassListView.as_view(), name = 'class_list_view'),
    path('classperiod/', ClassPeriodListView.as_view(), name = 'classperiod_list_view'),
    path('student/<int:id>/', StudentDetailView.as_view(),name ='student_detail_view')
    path('teacher/', TeacherListView.as_view(),name = 'teacher_list_view'),
]