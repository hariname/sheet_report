from django.contrib import admin
from .models import SheetReport
# Register your models here.

class SheetAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_no', 'name')
admin.site.register(SheetReport, SheetAdmin)
