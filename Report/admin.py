from django.contrib import admin

from .models import SheetReport, SiteInfo, LookUp


# Register your models here.


class LookUpAdmin(admin.ModelAdmin):
    list_display = ('title',)


class SiteAdmin(admin.ModelAdmin):
    list_display = ('site_title',)


class SheetAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_no', 'name')


admin.site.register(LookUp, LookUpAdmin)
admin.site.register(SiteInfo, SiteAdmin)
admin.site.register(SheetReport, SheetAdmin)
