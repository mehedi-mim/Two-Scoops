from django.db import models
from django.http.response import HttpResponseRedirect
from django.shortcuts  import render
from django.urls.base import is_valid_path
from .forms import StudentRegistration
# Create your models here.

def thankyou(request):
    return render(request,'enroll/success.html')

def showFormData(request):
    if (request.method) == 'POST':
        fm = StudentRegistration(request.POST)
        if(fm.is_valid()):
            print('From Validated')
            print('Name:',fm.cleaned_data['name'])
            print('Email:',fm.cleaned_data['email'])
            return HttpResponseRedirect('/regi/success/')
        else:
            fm = StudentRegistration()
        return render(request,'enroll/userregistration.html',{'form':fm})

