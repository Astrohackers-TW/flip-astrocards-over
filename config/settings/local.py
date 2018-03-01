"""
Local settings for astrocards project.

- Run in Debug mode

- Add Django Debug Toolbar
"""

from .base import *  # noqa

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/1.11/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env('DJANGO_SECRET_KEY', default='t3^5m+!%-we07o@31w4wdsv%p+dw8ov!$kbsn=00jaeubt+70m')

# DEBUG
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/1.11/ref/settings/#debug
DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
