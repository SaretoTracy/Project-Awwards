from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name = 'index'),
    path('projects/',views.projects,name = 'projects'),
    path('api/profile/', views.ProfileList.as_view()),
    path('details/<int:project_id>', views.project_details, name='image'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
  

    
]
