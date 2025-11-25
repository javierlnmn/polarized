from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    external_profile_picture_url = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    @property
    def profile_picture_url(self):
        return (
            self.external_profile_picture_url
            if self.external_profile_picture_url
            else "https://preview.redd.it/7ayjc8s4j2n61.png?auto=webp&s=609a58fa21d46424879ee44156e44e0404940583"
        )
