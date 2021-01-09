from collections import namedtuple

from django.shortcuts import render, redirect
from .models import Match, Player, Game


DemoPlayer = namedtuple("DemoPlayer", ["player", "played", "won", "lost"])


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


def players(request):
    players = Player.objects.all()
    players_data = []
    for player in players:
        played = Match.objects.filter(players__in=[player]).count()
        won = Match.objects.filter(winners__in=[player]).count()
        lost = played - won
        item = DemoPlayer(player=player, played=played, won=won, lost=lost)
        players_data.append(item)
    players_data = sorted(players_data, key=lambda x: x.won, reverse=True)
    context = {"players": players_data}
    return render(request, "players.html", context)


def gallery(request):
    games = Game.objects.all().order_by("name")
    context = {"games": games}
    return render(request, "gallery.html", context)

def game_detail(request, pk: int):
    """Game information page."""
    context = {"game": Game.objects.get(pk=pk)}
    return render(request, "game_detail.html", context)

def random_game(request):
    """Redirect to a game selected at random."""
    from random import choice

    pks = Game.objects.values_list('pk', flat=True)
    random_pk = choice(pks)
    return redirect('game_detail', pk=random_pk)
