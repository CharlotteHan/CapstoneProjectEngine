from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:project_id>/', views.detail, name='detail'),
    path('<int:project_id>/modify', views.modify, name='modify'),
    path('<int:project_id>/delete', views.delete, name='delete'),
    path('create/', views.create, name='create'),
    path('my_projects/', views.myprojects, name='myprojects'),
    path('my_project/', views.myproject, name='myproject'),
    path('project_list',views.project_list,name='project_list'),
    path('allocated',views.allocated,name='allocated'),
    path('unallocated',views.unallocated,name='unallocated'),
    path('<int:project_id>/allocate', views.allocate, name='allocate'),
    path('eoi_details/', views.eoi_details, name='eoi_details'),
    path('eoi/',views.eoi,name='eoi'),
    path('eoi_submitted/', views.eoi_submitted, name='eoi_submitted'),
]
