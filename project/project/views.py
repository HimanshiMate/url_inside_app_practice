from django.shortcuts import render
from django.http import HttpResponse
def projecthome(request):
    return HttpResponse("Welcome to the project home page")