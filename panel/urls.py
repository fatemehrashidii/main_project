from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('videos/', views.video, name='videos'),
    path('video/create', views.createVideo, name='create_video'),
path('video/<int:video_id>', views.videoDetail, name='teacher_video_details'),
    path('execise/', views.exercise, name='exercises'),
    path('exercise/create', views.createExercise, name='create_exercise'),
    path('response/', views.response, name='responses'),
    path('response/send', views.sendResponse, name='send_response'),

]

