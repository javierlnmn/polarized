from django.conf import settings


def site_settings(request):
    return {
        "google_oauth_client_id": settings.GOOGLE_OAUTH_CLIENT_ID,
        "schema": request.scheme,
        "current_host": request.get_host(),
        "full_url": f"{request.scheme}://{request.get_host()}",
        "full_url_with_path": request.build_absolute_uri(request.path),
    }
