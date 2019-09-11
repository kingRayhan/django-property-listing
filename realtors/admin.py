from django.contrib import admin
from .models import Realter
# Register your models here.


class RealterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_mvp')
    list_display_links = ('id', 'name',)
    list_filter = ('is_mvp',)
    list_editable = ('is_mvp',)
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(Realter, RealterAdmin)
