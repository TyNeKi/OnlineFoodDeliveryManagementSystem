from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        from django.contrib.auth.models import User
        from django.db.utils import OperationalError, ProgrammingError

        try:
            if not User.objects.filter(username='admin').exists():
                User.objects.create_superuser('admin', 'admin@example.com', '123456')
        except (OperationalError, ProgrammingError):
            pass
