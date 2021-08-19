from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

#FunctionBased View
def myview(request):
    return HttpResponse('<h1> Function based view </h1>')

#ClassBasedView

class MyView(View):
    def get(self,request):
        return HttpResponse('<h1> Class based view </h1>')

        
    