from telegram import InlineKeyboardButton, InlineKeyboardMarkup


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
    keyboard = [
        [InlineKeyboardButton('Мейкап', callback_data='Мейкап')],
        [InlineKeyboardButton('Покраска', callback_data='Покраска')],
        [InlineKeyboardButton('Маникюр', callback_data='Маникюр')]
    ]
    return InlineKeyboardMarkup(keyboard)


def get_data_keyboard():
    keyboard = [
        [InlineKeyboardButton('01.06', callback_data='01.06')],
        [InlineKeyboardButton('02.06', callback_data='02.06')],
        [InlineKeyboardButton('03.06', callback_data='03.06')]
    ]
    return InlineKeyboardMarkup(keyboard)


def get_time_keyboard():
    keyboard = [
        [InlineKeyboardButton('10:00', callback_data='10:00')],
        [InlineKeyboardButton('10:30', callback_data='10:30')],
        [InlineKeyboardButton('12:00', callback_data='12:00')]
    ]
    return InlineKeyboardMarkup(keyboard)


def get_master_keyboard():
    keyboard = [
        [InlineKeyboardButton('Ольга', callback_data='Ольга')],
        [InlineKeyboardButton('Татьяна', callback_data='Татьяна')]
    ]
    return InlineKeyboardMarkup(keyboard)
