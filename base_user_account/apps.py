from django.apps import AppConfig


class BaseUserAccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_user_account'
    verbose_name = 'پنل کاربران'
