from django.shortcuts import render

# Create your views here.
def doors(request):
    return render(request,'doors.html')

def login(request):
    return render(request,'login.html')

def section(request):
    return render(request,'section.html')

def signup(request):
    return render(request,'signup.html')
