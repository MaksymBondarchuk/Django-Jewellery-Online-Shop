from django.contrib import admin

from Shop.models import Metal, Jewel


class JewelAdmin(admin.ModelAdmin):
    """Customize the look of the auto-generated admin for the Member model"""
    list_display = ('name', 'instrument')
    list_filter = ('band',)

admin.site.register(Metal)
admin.site.register(Jewel)
