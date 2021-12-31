from django.shortcuts import render
from django.http import HttpResponse
from .models import Profiles

# Create your views here.

def home(request):
    # return HttpResponse('Home Page')
    profiles = Profiles.undeleted_objects.all()
    context={'profiles': profiles}
    return render(request, 'base/home.html', context)

def profile(request, pk):
    profile = Profiles.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'base/profile.html', context)
    # return HttpResponse('Profile Page')
