from django.urls import path
from example import views

urlpatterns = [
    path("", views.home, name='home'),
    path('projects/', views.projects, name='projects'),  # Projects view
    path('about/', views.about, name='about'),  # About view
    path('cv/', views.cv, name='cv'),
]
