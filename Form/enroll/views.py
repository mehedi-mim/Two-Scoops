from django.db import models
from django.shortcuts  import render
from .forms import StudentRegistration
# Create your models here.

def showFormData(request):
    fm = StudentRegistration()
    return render(request,'enroll/userregistration.html',{'form':fm})

