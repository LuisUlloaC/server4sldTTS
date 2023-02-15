from django.contrib import admin

# Register your models here.
from .models import Audio


class AudioAdmin(admin.ModelAdmin):
    pass

admin.site.register(Audio, AudioAdmin)