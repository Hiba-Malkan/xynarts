from django.contrib import admin
from django.utils.html import format_html
from .models import SiteSettings

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Banner', {
            'fields': ('title', 'icon', 'role_line1', 'role_line2', 'banner', 'banner_preview'),
        }),
        ('About Section', {
            'fields': ('about_heading', 'about_text', 'about_photo', 'photo_preview', 'about_signature', 'signature_preview'),
        }),

    ]
    readonly_fields = ('banner_preview', 'photo_preview', 'signature_preview')
    def banner_preview(self, obj):
        if obj.banner: 
            return format_html('<img src="{}" style="max-width: 200px; max-width: 400px; object-fit: cover; border-radius: 6px;"/>', obj.banner.url)
        return "-"
    banner_preview_short_description = 'Banner Preview'
    
    def photo_preview(self, obj):
        if obj.about_photo:
            return format_html('<img src="{}" style="max-height: 200px; border-radius: 12px;"/>', obj.about_photo.url)
        return "-"
    photo_preview_short_description = 'Photo Preview'

    def signature_preview(self, obj):
        if obj.about_signature:
            return format_html('<img src="{}" style="max-height: 60px;"/>', obj.about_signature.url)
        return "-"
    signature_preview_short_description = 'Signature Preview'

    def has_add_permission(self, request):
        if SiteSettings.objects.count() > 0:
            return False
        return True
    
    def has_delete_permission(self, request, obj=None):
        return False
