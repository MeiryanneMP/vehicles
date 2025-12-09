from django.contrib import admin
from vehicles.models import Vehicle, Brand


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'price')
    search_fields = ('model',)


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Brand, BrandAdmin)
