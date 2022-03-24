from django.contrib import admin
from django.urls import path
from .views import Books_list_View


urlpatterns = [
    path('test', Books_list_View.as_view()),
]
