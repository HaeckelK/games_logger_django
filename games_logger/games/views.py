from django.shortcuts import render
from .models import Match, Player


def hello_world(request):
    return render(request, 'hello_world.html', {})


def index(request):
    """Landing page"""
    n = int(request.GET.get("n", 5))
    context = {"matches": Match.objects.order_by('-created_on')[:n]}
    return render(request, "index.html", context)


def player_detail(request, pk: int):
    """Player information page."""
    played = Match.objects.filter(players__in=[pk]).count()
    won = Match.objects.filter(winners__in=[pk]).count()
    context = {"player": Player.objects.get(pk=pk),
               "played": played,
               "won": won}
    return render(request, "player.html", context)
