from django.contrib import admin
from .models import Listing
# Register your models here.


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'city',
                    'price', 'realtor', 'photo_main', 'zipcode')
    list_display_links = ('id', 'title',)
    list_filter = ('realtor', 'is_published', 'city')
    list_editable = ('is_published', 'realtor')
    search_fields = ('title', 'description', 'city', 'zipcode')
    save_on_top = True


admin.site.register(Listing, ListingAdmin)
