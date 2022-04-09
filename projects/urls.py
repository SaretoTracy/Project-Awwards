from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name = 'index'),
    path('projects/',views.projects,name = 'projects'),
    path('api/profile/', views.ProfileList.as_view()),
    path('image/<int:image_id>', views.project_details, name='image'),
  

    
]
