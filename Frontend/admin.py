from django.contrib import admin
from .models import prijzen, contact

class prijzenAdmin(admin.ModelAdmin):
    list_display = ('titel',)

class contactAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(prijzen, prijzenAdmin)
admin.site.register(contact, contactAdmin)