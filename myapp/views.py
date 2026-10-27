from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to the Home Page!</h1>")


def about(request):
    return HttpResponse("<h1>About Page</h1>")


def health(request):
    return JsonResponse({"status": "ok"})
