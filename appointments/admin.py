from django.contrib import admin

from .models import Client, Master, Service, Saloon, Slot

admin.site.register(Client)
admin.site.register(Master)
admin.site.register(Service)
admin.site.register(Saloon)
admin.site.register(Slot)
