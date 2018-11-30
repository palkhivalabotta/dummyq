from django.contrib import admin

from .models import Hotels
from .models import Room


# Register your models here.
admin.site.register(Hotels)
admin.site.register(Room)
