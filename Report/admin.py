from django.contrib import admin

from .models import SheetReport, SiteInfo


# Register your models here.

class SheetAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_no', 'name')


class SiteAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(SiteInfo, SiteAdmin)
admin.site.register(SheetReport, SheetAdmin)
