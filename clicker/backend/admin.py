from django.contrib import admin
from .models import Core, Boost, AutoBoost

# Register your models here.

admin.site.register(Core)
admin.site.register(Boost)
admin.site.register(AutoBoost)