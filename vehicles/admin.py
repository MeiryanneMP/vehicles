from django.contrib import admin
from vehicles.models import Vehicle


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'price')
    search_fields = ('model',)


admin.site.register(Vehicle, VehicleAdmin)
