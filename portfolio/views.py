from django.shortcuts import render
from .models import SiteSettings


def site_settings(request): 
    try: 
        settings = SiteSettings.objects.first()
    except Exception:
        settings = None
    return {
        'site': settings
    }
    
def index(request):
    return render(request, 'index.html')