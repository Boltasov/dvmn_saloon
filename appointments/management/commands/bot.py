from django.core.management import BaseCommand

from appointments import telegram_bot
from appointments.telegram_bot import main


class Command(BaseCommand):
    help = 'Запуск телеграм-бота'

    def handle(self, *args, **options):
        main.start_bot()
