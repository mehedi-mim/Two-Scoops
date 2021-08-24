from enroll.forms import StudentRegistration
from django.shortcuts import render,HttpResponseRedirect
from .models import User

# Create your views here.

def  add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
        
    return render(request,'enroll/addandshow.html', {'form':fm,'stu':stud})



def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk = id)
        pi.delete()
        return HttpResponseRedirect('/')