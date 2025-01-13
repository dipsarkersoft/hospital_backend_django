from django.contrib import admin
from . import models
# Register your models here.

class DesigationAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',),}


class SpeacializationAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',),}


admin.site.register(models.AvailableTime)
admin.site.register(models.Desigation,DesigationAdmin)
admin.site.register(models.Speacialization,SpeacializationAdmin)
admin.site.register(models.Doctor)
admin.site.register(models.Review)

