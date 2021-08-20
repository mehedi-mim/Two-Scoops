from django.urls import path 
from .import views

urlpatterns = [
    path('registration/',views.showFormData),
    path('success/',views.thankyou)

]