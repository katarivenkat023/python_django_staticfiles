from django.shortcuts import render

# Create your views here.
def static(request):
    d={'name':'venkat'}
    return render(request,'file.html',d)