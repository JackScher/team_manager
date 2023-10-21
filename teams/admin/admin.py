from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .forms import TeamAdminForm
from teams.models import Team


@admin.register(Team)
class TeamModelADmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    form = TeamAdminForm
    fieldsets = (
        (
            _('System Attributes'), 
            {
                'fields': ('id',)
            }
        ),
        (
            _('Properties'),
            {
                'fields': ('name', 'persons',)
            }
        ),
    )
    list_display = ('name', 'related_persons')
    search_fields = ('name',)
    ordering = ('name',)
