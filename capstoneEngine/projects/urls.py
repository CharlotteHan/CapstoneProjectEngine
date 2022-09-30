from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:project_id>/', views.detail, name='detail'),
    path('<int:project_id>/modify', views.modify, name='modify'),
    path('create/', views.create, name='create'),
    path('my_projects/', views.myprojects, name='myprojects'),
    path('my_project/', views.myproject, name='myproject'),
    path('eoi/',views.eoi,name='eoi'),
]
