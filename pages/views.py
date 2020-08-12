from django.shortcuts import render
import httpResponse by:from django.http import HttpResponse

def index(request):
  return render(request,'pages/index.html')