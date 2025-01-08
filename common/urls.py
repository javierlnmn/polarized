from django.urls import path

from django.conf.urls.i18n import set_language


app_name = 'common'

urlpatterns = [
    path('set-language/', set_language, name='set_language'),
]
