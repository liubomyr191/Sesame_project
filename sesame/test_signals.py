import hashlib

from django.conf import settings
from django.core.signals import setting_changed
from django.dispatch import receiver

from .backends import UrlAuthBackendMixin


@receiver(setting_changed)
def reset_sesame_settings(**kwargs):
    UABM = UrlAuthBackendMixin

    if kwargs['setting'] == 'SESAME_SALT':
        UABM.salt = getattr(settings, 'SESAME_SALT', 'sesame')
    elif kwargs['setting'] == 'SESAME_DIGEST':
        UABM.digest = getattr(settings, 'SESAME_DIGEST', hashlib.md5)
    elif kwargs['setting'] == 'SESAME_ITERATIONS':
        UABM.iterations = getattr(settings, 'SESAME_ITERATIONS', 10000)

    elif kwargs['setting'] == 'SESAME_MAX_AGE':
        UABM.max_age = getattr(settings, 'SESAME_MAX_AGE', None)
    elif kwargs['setting'] == 'SESAME_ONE_TIME':
        UABM.one_time = getattr(settings, 'SESAME_ONE_TIME', False)
    elif kwargs['setting'] == 'SESAME_INVALIDATE_ON_PASSWORD_CHANGE':
        UABM.invalidate_on_password_change = getattr(
            settings, 'SESAME_INVALIDATE_ON_PASSWORD_CHANGE', True)
