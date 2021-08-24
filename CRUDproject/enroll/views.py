from enroll.forms import StudentRegistration
from django.shortcuts import render

# Create your views here.

def  add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
    else:
        fm = StudentRegistration()
    return render(request,'enroll/addandshow.html', {'form':fm})
    