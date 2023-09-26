from django.contrib import admin
from billing.models import Price 

# Register your models here.
class PriceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'created_at', 'unit_price')
    readonly_fields = ['created_at']
    search_fields = ['service_name']

admin.site.register(Price, PriceAdmin)
