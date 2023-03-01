from django import forms
from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest
from . import models


class MenuItemContainerForm(forms.ModelForm):
    class Meta:
        model = models.MenuItemContainer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # exclude menu items from other menus
        if self.instance:
            self.fields['parent_item'].queryset = models.MenuItemContainer.objects.filter(menu_id=self.instance.menu_id)


class MenuItemContainerInline(admin.TabularInline):
    model = models.MenuItemContainer
    form = MenuItemContainerForm
    extra = 0


@admin.register(models.NestedMenu)
class NestedMenuAdmin(admin.ModelAdmin):
    list_display = 'id', 'name',
    list_editable = 'name',
    inlines = MenuItemContainerInline,
