from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.projecthomepage,name ='projecthomepage'),
    path('employerhomepage',views.employerhomepage,name ='employerhomepage'),
    path('jobseekerhomepage',views.jobseekerhomepage,name ='jobseekerhomepage')
    ]



