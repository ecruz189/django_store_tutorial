from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler
# action (in some frameworks)

def say_hello(request):
    # Options of what can be done
    # Pull data from db
    # Transform
    # Send email
    return render(request, 'hello.html', {'name': 'Mosh'})
