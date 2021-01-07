from django.contrib import admin
from games.models import Player, Game, Match, TimeCategory, GenreCategory, PlatformCategory

class PlayerAdmin(admin.ModelAdmin):
    pass

class GameAdmin(admin.ModelAdmin):
    pass

class MatchAdmin(admin.ModelAdmin):
    pass

class TimeCategoryAdmin(admin.ModelAdmin):
    pass

class GenreCategoryAdmin(admin.ModelAdmin):
    pass

class PlatformCategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Player, PlayerAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(TimeCategory, TimeCategoryAdmin)
admin.site.register(GenreCategory, GenreCategoryAdmin)
admin.site.register(PlatformCategory, PlatformCategoryAdmin)
