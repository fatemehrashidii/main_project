from django.shortcuts import render
from .forms import UploadVideoForm
from django.http import HttpResponse, JsonResponse

#####2
from .models import *


#from .forms import UploadVideoForm
from .forms import *


def home(request):
    return render(request, "panel/home.html")

def video(request):
    form = Videos.objects.all()
    context = {'video': form}
    return render(request, 'panel/video.html', context)

def createVideo(request):
    form = UploadVideoForm()
    if request.method == "POST":
        form = UploadVideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('video has been uploaded successfully.')
    context = {'form': form}
    return render(request, "panel/create_video.html", context)

def videoDetail(request, video_id):
    vid = Videos.objects.get(id=video_id)
    context = {'video': vid}
    return render(request, 'panel/teacher_video_details.html', context)

def exercise(request):
    form = Exercises.objects.all()
    context = {'exercise': form}
    return render(request, "panel/exercise.html", context)

def createExercise(request):
    form = UploadExerciseForm()
    if request.method == "POST":
        form = UploadExerciseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('exercise has been uploaded successfully.')
    context = {'form': form}
    return render(request, "panel/create_exercise.html", context)


def response(request):
    form = Responses.objects.all()
    context = {'response': form}
    return render(request, "panel/response.html", context)


def sendResponse(request):
    form = SendResponseForm()
    if request.method == "POST":
        form = SendResponseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('file has been uploaded successfully.')
    context = {'form': form}
    return render(request, "panel/send_response.html", context)


#def student(request):
 #   form = Student_Login.objects.all()
  #  context = {'form': form}
   # return render(request,"panel/student.html", context)

#def StudentLogin(request):
 #   form = StudentLoginForm()
   # if request.method == "POST":
  #      form = StudentLoginForm(request.POST)    ####request.FILES
 #       if form.is_valid():
#            form.save()
   # context = {'form': form}
  #  return render(request, "panel/StudentLogin.html", context)


#def TeacherLogin(request):
 #   form = TeacherLoginForm()
  #  context = {'form': form}
   # return render(request, "panel/TeacherLogin.html", context)



#def Results(request):
 #   form = ResultsForm()
  #  context = {'form': form}
    #return render(request, "panel/results.html", context)