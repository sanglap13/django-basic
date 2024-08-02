from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.allWork, name="allWork"),
    path('<int:work_id>/', views.workDetails, name="workDetails"),
    
]
