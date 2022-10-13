from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """
    It takes a request object as an argument, and returns an HttpResponse object
    param request: The request object is an HttpRequest object. 
    It contains metadata about the request
    return: The request object.
    """
    return HttpResponse("yayyyyyyyyy")
