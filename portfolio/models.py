from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=50, default = "XYN ARTS")
    icon = models.CharField(max_length=50, default='✦')
    role_line1 = models.CharField(max_length=30, default = "DIGITAL")
    role_line2 = models.CharField(max_length=30, default = "ILLUSTRATOR")
    banner = models.ImageField(upload_to='banner/', blank=True)
    
    class Meta: 
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.title
    
    def save (self, *args, **kwargs):
        if not self.pk and Project.objects.exists():
            return

        super().save(*args, **kwargs)
