from django.contrib import admin
from .models import Travel
# Register your models here.
class TravelAdmin(admin.ModelAdmin):
    list_display = ("travelTitle", "travelDesc", "travelAddress", "travelImg")
admin.site.register(Travel)