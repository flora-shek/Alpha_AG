from django.shortcuts import render



def index(request):
    return render(request,'layout.html')

def submit(request):
    return render(request,'layout.html')