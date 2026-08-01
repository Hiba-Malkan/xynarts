from django.contrib import admin
from django.utils.html import format_html
from .models import SiteSettings

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Settings', {
            'fields': ('title', 'icon', 'role_line1', 'role_line2', 'banner', 'banner_preview'),
        })
    ]
    readonly_fields = ('banner_preview',)
    def banner_preview(self, obj):
        if obj.hero.banner: 
            return format_html('<img src="{}" style="max-width: 200px; max-width: 400px; object-fit: cover; border-radius: 6px;"/>', obj.hero.banner.url)
        return "-"
    banner_preview_short_description = 'Banner Preview'
    
    def has_add_permission(self, request):
        if SiteSettings.objects.count() > 0:
            return False
        return True
    
    def has_delete_permission(self, request, obj=None):
        return False
