from django.shortcuts import render
from .models import Match


def hello_world(request):
    return render(request, 'hello_world.html', {})


def index(request):
    """Landing page"""
    n = int(request.GET.get("n", 5))
    context = {"matches": Match.objects.order_by('-created_on')[:n]}
    return render(request, "index.html", context)
