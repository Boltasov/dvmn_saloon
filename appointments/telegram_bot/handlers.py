from re import match
from datetime import datetime

from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import ConversationHandler

from appointments.telegram_bot.keyboards import BOOK_SLOT_BUTTON, BOOK_MASTER_BUTTON, ABOUT_BUTTON
from appointments.telegram_bot.keyboards import get_start_keyboard, get_service_keyboard, get_data_keyboard, \
    get_master_keyboard, get_time_keyboard
from appointments.models import Slot, Client, Master, Service, Saloon


MENU, ASK_SERVICE, ASK_DATE, ASK_TIME, ASK_MASTER, ASK_PHONE = range(6)


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Здравствуйте!\n\n Выберите один из вариантов записи с помощью кнопок.",
                             reply_markup=get_start_keyboard())
    return MENU


def keyboard_menu_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data
    chat_id = update.effective_message.chat_id
    current_text = update.effective_message.text

    if data == BOOK_SLOT_BUTTON:
        context.user_data['way'] = 'slot'
        query.edit_message_text(text=current_text)
        context.bot.send_message(chat_id=chat_id,
                                 text='Выбор процедуры',
                                 reply_markup=get_service_keyboard())
        return ASK_SERVICE
    elif data == BOOK_MASTER_BUTTON:
        context.user_data['way'] = 'master'
        query.edit_message_text(text=current_text)
        context.bot.send_message(chat_id=chat_id,
                                 text='Выбор мастера',
                                 reply_markup=get_master_keyboard())
        return ASK_MASTER
    elif data == ABOUT_BUTTON:
        context.bot.send_message(chat_id=chat_id,
                                 text='О нас')


def keyboard_service_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data
    chat_id = update.effective_message.chat_id
    current_text = update.effective_message.text

    context.user_data['service'] = data
    query.edit_message_text(text=current_text)
    context.bot.send_message(chat_id=chat_id,
                             text=f'Сервис: {data} Выбор даты',
                             reply_markup=get_data_keyboard()
                             )
    return ASK_DATE


def keyboard_date_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data
    chat_id = update.effective_message.chat_id
    current_text = update.effective_message.text

    context.user_data['date'] = data
    slot_date = datetime.strptime(data, '%d.%m.%Y')
    query.edit_message_text(text=current_text)
    context.bot.send_message(chat_id=chat_id,
                             text='Сервис: {}. Дата: {}. Выбор времени'.format(context.user_data['service'], data),
                             reply_markup=get_time_keyboard(slot_date)
                             )
    return ASK_TIME


def message_date_handler(update: Update, context: CallbackContext):
    text = update.message.text
    if match(r'\d\d\.\d\d\.\d\d\d\d', update.message.text):
        context.user_data['date'] = text
        slot_date = datetime.strptime(text, '%d.%m.%Y')
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Сервис: {}. Дата: {}. Выбор времени'
                                 .format(context.user_data['service'], context.user_data['date']),
                                 reply_markup=get_time_keyboard(slot_date)
                                 )
        return ASK_TIME
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Бот не очень умный. Введите, пожалуйста, дату в формате: "dd.mm.yyyy".\n'
                                      'Например: 01.06.2023')


def keyboard_time_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data
    chat_id = update.effective_message.chat_id
    current_text = update.effective_message.text

    context.user_data['time'] = data
    query.edit_message_text(text=current_text)
    if context.user_data['way'] == 'slot':
        context.bot.send_message(chat_id=chat_id,
                                 text='Сервис: {}. Дата: {}. Время: {}. Выберите мастера:'
                                 .format(context.user_data['service'], context.user_data['date'], data),
                                 reply_markup=get_master_keyboard()
                                 )
        return ASK_MASTER
    elif context.user_data['way'] == 'master':
        context.bot.send_message(chat_id=chat_id, text='Укажите телефон')
        return ASK_PHONE


def message_time_handler(update: Update, context: CallbackContext):
    text = update.message.text
    chat_id = update.effective_message.chat_id
    if match(r'\d\d:\d\d', update.message.text):
        context.user_data['time'] = text
        if context.user_data['way'] == 'slot':
            context.bot.send_message(chat_id=chat_id,
                                     text='Сервис: {}. Дата: {}. Время: {}. Выберите мастера:'
                                     .format(context.user_data['service'],
                                             context.user_data['date'],
                                             context.user_data['time']),
                                     reply_markup=get_master_keyboard()
                                     )
            return ASK_MASTER
        elif context.user_data['way'] == 'master':
            context.bot.send_message(chat_id=chat_id, text='Укажите телефон')
            return ASK_PHONE
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Бот не очень умный. Введите, пожалуйста, время в формате: "hh:mm"\n'
                                      'Например: 14:30')


def keyboard_master_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data
    chat_id = update.effective_message.chat_id
    current_text = update.effective_message.text

    context.user_data['master'] = data
    query.edit_message_text(text=current_text)
    if context.user_data['way'] == 'slot':
        context.bot.send_message(chat_id=chat_id,
                                 text='Сервис: {}. Дата: {}. Время: {}. Мастер: {}. Укажите телефон:'
                                 .format(context.user_data['service'], context.user_data['date'],
                                         context.user_data['time'], data)
                                 )
        return ASK_PHONE
    elif context.user_data['way'] == 'master':
        context.bot.send_message(chat_id=chat_id, text='Выберите процедуру', reply_markup=get_service_keyboard())
        return ASK_SERVICE


def phone_handler(update: Update, context: CallbackContext):
    text = update.message.text
    if text.isnumeric() and len(text) == 11:
        phone = update.message.text
        service = context.user_data['service']
        time = datetime.strptime(context.user_data['time'], '%H:%M').time()
        date = datetime.strptime(context.user_data['date'], '%d.%m.%Y').date()
        slot_datetime = datetime.combine(date, time)
        master = context.user_data['master']

        slot = Slot.objects.filter(start_datetime=slot_datetime).first()
        slot.client, _ = Client.objects.get_or_create(phone_number=phone)
        slot.master = Master.objects.get(pk=master)
        slot.service = Service.objects.get(pk=service)
        slot.save()
        print('Slot: ', slot.pk, slot.master.pk)

        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Успешная запись\n\nСервис: {}.\nВремя: {} {}.\nМастер: {}.\nВаш телефон: {}"
                                 .format(service,
                                         context.user_data['date'],
                                         context.user_data['time'],
                                         master,
                                         phone)
                                 )
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Можете создать ещё одну запись с помощью команды /start.")
        return ConversationHandler.END
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Бот не очень умный. '
                                      'Введите, пожалуйста, номер телефона в формате: "78005553535"')


def cancel_handler(update: Update, context: CallbackContext):
    """ Отменить весь процесс диалога. Данные будут утеряны
    """
    update.message.reply_text('Отмена. Для начала с нуля введите /start')
    return ConversationHandler.END
