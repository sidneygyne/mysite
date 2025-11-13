from blog import views
from blog import views_exercise
from django.urls import path

urlpatterns = [
    path('', views.PostView.as_view(), name='home'),
    path("<slug:slug>/", views.PostDetail.as_view(), name='post_detail'),
]
