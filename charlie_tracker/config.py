"""
Configuration for Charlie Tracker (i.e. API keys)
"""

import os

CONFIG_KEYS = {
    # MBTA API Key
    'CT_MBTA_API_KEY': None,

}

def configure() -> None:
    """
    Configure the application using a three way try for settings.
    """
    prefer_django = True
    try:
        from django.conf import settings
    except ImportError:
        prefer_django = False

    if prefer_django:
        primary_config = settings
        fallback_config = os.environ
    else:
        primary_config = os.environ
        fallback_config = os.environ

    for key, default_value in CONFIG_KEYS.items():
        value = primary_config.get(
            key,
            fallback_config.get(key, default_value)
        )
        globals()[key] = value

configure()
