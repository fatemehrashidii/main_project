from django import forms
from django.forms import ModelForm
from .models import *

class UploadVideoForm(ModelForm):
    class Meta:
        model = Videos
        fields = '__all__'


class UploadExerciseForm(ModelForm):
    class Meta:
        model = Exercises
        fields = '__all__'


class SendResponseForm(ModelForm):
    class Meta:
        model = Responses
        fields = '__all__'



#class StudentLoginForm(ModelForm):
   # class Meta:
  #      model = Student_Login
 #       fields = '__all__'

#class TeacherLoginForm(ModelForm):
  #  class Meta:
 #       model = Teacher_Login
#        fields = '__all__'

#class SendResponseForm(ModelForm):
 #   class Meta:
  #      model = Send_Response
   #     fields = ['title', 'response']


class WatchVideoForm(ModelForm):
    class Meta:
        model = Watch_Videos
        fields = '__all__'

class ResultsForm(ModelForm):
    class Meta:
        model = Results
        fields = '__all__'

