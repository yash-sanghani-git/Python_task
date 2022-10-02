from django.urls import re_path
from python_task import views

urlpatterns = [
    re_path(r'GetSheet/', views.GetSheet.as_view()),
]
