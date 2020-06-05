from django.contrib import admin
from django.urls import path
from .views import Chatview
urlpatterns = [
    path('chat/',Chatview.as_view(),name="chat"),
]