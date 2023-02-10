from django.contrib import admin
from .models import Site, order, iap, switch
# Register your models here.
admin.site.register(Site)
admin.site.register(order)
admin.site.register(iap)
admin.site.register(switch)
