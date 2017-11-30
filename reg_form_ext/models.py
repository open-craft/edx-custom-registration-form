from django.conf import settings
from django.db import models

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class PhoneInfo(models.Model):
    """
    Holds phone number with country code.
    Used during user registration as a form extension.
    """
    user = models.OneToOneField(USER_MODEL, null=True)
    country_code = models.CharField(
        verbose_name="Country Calling Code",
        max_length=7
    )
    phone_number = models.CharField(
        verbose_name="Phone Number",
        max_length=60
    )
