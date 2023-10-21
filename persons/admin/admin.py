from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from persons.models import Person


@admin.register(Person)
class PersonModelADmin(admin.ModelAdmin):
    readonly_fields = ('id',)
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
                'fields': ('email', 'first_name', 'last_name')
            }
        ),
    )
    list_display = ('email', 'first_name', 'last_name')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
