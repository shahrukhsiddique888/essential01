from django.contrib import admin
from . import models
# Register your models here.
class adminNotes(admin.ModelAdmin):
    pass

admin.site.register(models.notes, adminNotes)