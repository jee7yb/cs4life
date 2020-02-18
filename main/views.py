from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader

# Create your views here.
def login(request):
    return render(request, 'login/index.html')

def loggedin(request):
    #add code to store info from google into models
    #profile = googleUser.getBasicProfile()
    #if form not complete for user -> render form page
    if(request.method == "POST"):
        name = request.POST['Name']
        email = request.POST['Email']
        image = request.POST['Image']
        ID = request.POST['ID']
    return HttpResponseRedirect(reverse('login:home'))

def home(request):
    return render(request, 'login/home.html')