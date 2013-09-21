from django.conf import settings


def api_keys(request):
    return {
        "GOOGLE_API_KEY": settings.GOOGLE_API_KEY
    }