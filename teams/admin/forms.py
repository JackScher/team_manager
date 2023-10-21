from django.contrib import admin
from django.forms import ModelForm, ModelMultipleChoiceField
from teams.models import Team


class TeamAdminForm(ModelForm):
    persons = ModelMultipleChoiceField(
        queryset=Team.persons.field.related_model.objects.all(),
        widget=admin.widgets.FilteredSelectMultiple("persons", is_stacked=False),
        required=False,
    )
