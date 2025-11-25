from django.conf.urls.i18n import set_language
from django.urls import path

app_name = "common"

urlpatterns = [
    path("set-language/", set_language, name="set_language"),
]
