from blog import views
from blog import views_exercise
from django.urls import path

urlpatterns = [
    path('', views.PostView.as_view(), name='home'),
    path('exercise/', views_exercise.PostViewExercise.as_view(), name='exercise'),
]
