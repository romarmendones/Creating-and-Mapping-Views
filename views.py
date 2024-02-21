from django.shortcuts import render
from django.http import HttpResponse

def mission_view(request):
    return HttpResponse("CCMS Mission")

def vision_view(request):
    return HttpResponse("CCMS Vision")

def objectives_view(request):
    return HttpResponse("CCMS Objectives")
