from django.contrib import admin

from Shop.models import Metal, Jewel


class MetalAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Metal, MetalAdmin)


class JewelAdmin(admin.ModelAdmin):
    list_display = ['name', 'metal_name', 'fineness', 'description', 'image']
    list_filter = ['name']
    ordering = ['name']
    list_display_links = ['name', 'metal_name']

    @staticmethod
    def metal_name(obj):
        return obj.metal.name
admin.site.register(Jewel, JewelAdmin)
