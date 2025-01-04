from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login
from django.conf import settings

from google.oauth2 import id_token
from google.auth.transport import requests

from .models import CustomUser


@csrf_exempt
def google_auth_receiver(request):
    token = request.POST['credential']

    try:
        user_data = id_token.verify_oauth2_token(token, requests.Request(), settings.GOOGLE_OAUTH_CLIENT_ID)
    except ValueError:
        return HttpResponse(status=403)

    email = user_data.get('email')
    first_name = user_data.get('given_name', '')
    last_name = user_data.get('family_name', '')
    profile_picture_url = user_data.get('picture', None)

    user, created = CustomUser.objects.get_or_create(
        username=email,
        defaults={
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'external_profile_picture_url': profile_picture_url
        }
    )

    login(request, user)

    return redirect('common:index')