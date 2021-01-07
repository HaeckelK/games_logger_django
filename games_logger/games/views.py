from django.shortcuts import render


def hello_world(request):
    return render(request, 'hello_world.html', {})


def index(request):
    """Landing page"""
    return render(request, "index.html", {})
