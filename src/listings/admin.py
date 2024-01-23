from django.contrib import admin
from .models import Band
from .models import Listing

# Register your models here.

class BandAdmin(admin.ModelAdmin):
  list_display = ("name","genre","year_formed")
  
class ListingAdmin(admin.ModelAdmin):
  list_display = ("title","types","band")
admin.site.register(Band,BandAdmin)
admin.site.register(Listing,ListingAdmin)