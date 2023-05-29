from datetime import datetime

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from appointments.models import Slot, Master, Service


BOOK_SLOT_BUTTON = 'book'
BOOK_MASTER_BUTTON = 'master'
ABOUT_BUTTON = 'about'

TITLES = {
    BOOK_SLOT_BUTTON: 'Записаться',
    BOOK_MASTER_BUTTON: 'Выбрать мастера',
    ABOUT_BUTTON: 'О нас'
}


def get_start_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(TITLES[BOOK_SLOT_BUTTON], callback_data=BOOK_SLOT_BUTTON),
            InlineKeyboardButton(TITLES[BOOK_MASTER_BUTTON], callback_data=BOOK_MASTER_BUTTON)
        ],
        [
            InlineKeyboardButton(TITLES[ABOUT_BUTTON], callback_data=ABOUT_BUTTON)
        ]
    ]

    return InlineKeyboardMarkup(keyboard)


def get_service_keyboard():
    services = Service.objects.all()
    keyboard = []
    for service in services:
        keyboard.append([InlineKeyboardButton(service.name, callback_data=service.pk)])

    return InlineKeyboardMarkup(keyboard)


def get_data_keyboard(master=None):
    now = datetime.now()
    if master:
        actual_dates = Slot.objects.filter(start_datetime__gte=now).filter(client=None).filter(master=master)
    else:
        actual_dates = Slot.objects.filter(start_datetime__gte=now).filter(client=None)
    min_date = actual_dates.order_by('start_datetime').first()
    date = min_date.start_datetime.strftime("%d.%m.%Y")
    keyboard = [
        [InlineKeyboardButton(date, callback_data=date)],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_time_keyboard(date: datetime, master=None):
    if master:
        actual_dates = Slot.objects.filter(start_datetime__gte=date).filter(client=None).filter(master=master)
    else:
        actual_dates = Slot.objects.filter(start_datetime__gte=date).filter(client=None)
    min_date = actual_dates.order_by('start_datetime').first()
    slot_time = min_date.start_datetime.strftime('%H:%M')
    keyboard = [
        [InlineKeyboardButton(slot_time, callback_data=slot_time)]
    ]
    return InlineKeyboardMarkup(keyboard)


def get_master_keyboard():
    masters = Master.objects.all()
    keyboard = []
    for master in masters:
        keyboard.append([InlineKeyboardButton(master.name, callback_data=master.pk)])

    return InlineKeyboardMarkup(keyboard)
