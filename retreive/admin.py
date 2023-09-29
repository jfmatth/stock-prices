# Register your models here.
from django.contrib import admin
from retreive.models import Price, Retreive

class PriceAdmin(admin.ModelAdmin):
    pass

class RetreiveAdmin(admin.ModelAdmin):
    pass

admin.site.register(Price, PriceAdmin)
admin.site.register(Retreive, RetreiveAdmin)