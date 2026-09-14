from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('projects/<int:id>/',views.project_detail,name='project_detail'),
    path('certifications/<int:id>/', views.certification_detail, name='certification_detail')
]




