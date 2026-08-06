from django.db import models

class SiteSettings(models.Model):
    title = models.CharField(max_length=50, default = "XYN ARTS")
    subtitle = models.CharField(max_length=50, default = "PORTFOLIO")
    icon = models.CharField(max_length=50, default='✦')
    role_line1 = models.CharField(max_length=30, default = "DIGITAL")
    role_line2 = models.CharField(max_length=30, default = "ILLUSTRATOR")
    banner = models.ImageField(upload_to='banner/', blank=True)
    about_heading = models.CharField(max_length=50, default = "ABOUT ME")
    about_text = models.TextField(default = '')
    about_photo = models.ImageField(upload_to='about/', blank=True)
    about_signature = models.ImageField(upload_to='about/', blank=True)
    
    class Meta: 
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.title
    
    def save (self, *args, **kwargs):
        if not self.pk and SiteSettings.objects.exists():
            return

        super().save(*args, **kwargs)
