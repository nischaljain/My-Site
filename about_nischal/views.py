from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'about_nischal/index.html')

def projects(request):
    return render(request,'about_nischal/projects.html')