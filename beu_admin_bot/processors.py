from django_tgbot.decorators import processor
from django_tgbot.state_manager import message_types, update_types, state_types
from django_tgbot.types.update import Update
from .bot import state_manager
from .models import TelegramState
from .bot import TelegramBot
from django_tgbot.types.keyboardbutton import KeyboardButton
from django_tgbot.types.replykeyboardmarkup import ReplyKeyboardMarkup
from django_tgbot.types.inlinekeyboardbutton import InlineKeyboardButton
from django_tgbot.types.inlinekeyboardmarkup import InlineKeyboardMarkup
from our_beu_delivery_bot.models import Order, Restaurant

@processor(state_manager, success='asked_for_contact', message_types=[message_types.Text])
def initial_setup(bot: TelegramBot, update: Update, state: TelegramState):
    chat_id = update.get_chat().get_id()
    bot.sendMessage(chat_id, 'Hello there, Welcome to the beu admin control bot  :)')
    bot.sendMessage(chat_id, " You can't access this bot unless you are an owner of a restaurant :)")
    bot.sendMessage(chat_id, " Enter your phone number down here to let me know if this bot is for you...")
    """
    bot.sendMessage(
        chat_id,
        text="Hit the button below to let me know if you're an admin",
        reply_markup=ReplyKeyboardMarkup.a(
            one_time_keyboard=True,
            resize_keyboard=True,
            keyboard=[
                [KeyboardButton.a(text='Share my phone number', request_contact=True)],
            ]
        )
    )
    """

@processor(state_manager, from_states='asked_for_contact', message_types=message_types.Text)
def get_contact(bot, update, state):
    chat_id = update.get_chat().get_id()
    phone = update.get_message().get_text()
    found = False
    for rest in Restaurant.objects.all():
        if phone == rest.phone_num:
            found = True
            state.set_name('next_steps')
            state.set_memory({
                    'rest': rest.name
                })
            bot.sendMessage(chat_id, "Welcome to this admin bot :)")
            bot.sendMessage(chat_id, f"You must be the owner or staff of {rest.name}")
            bot.sendMessage(
                chat_id,
                text='Here is a keyboard for you!',
                reply_markup=ReplyKeyboardMarkup.a(
                    one_time_keyboard=True,
                    resize_keyboard=True,
                    keyboard=[
                        [KeyboardButton.a('Add new food to catalogue')],
                        [KeyboardButton.a('View pending orders')],
                        [KeyboardButton.a('Visit admin webpage')]
                    ]
                )
            )

    if not found:
        state.set_name('asked_for_contact')
        bot.sendMessage(chat_id, "You should not be here (:")
        bot.sendMessage(chat_id, "This is the admin bot for another bot which enables users to submit orders for restaurants (:")
        bot.sendMessage(
            chat_id,
            text='This is the bot for users to submit orders',
            reply_markup=InlineKeyboardMarkup.a(
                inline_keyboard=[
                    [
                        InlineKeyboardButton.a('@our_beu_delivery_bot', url='t.me/our_beu_delivery_bot'),

                    ]
                ]
            )
        )

@processor(state_manager, from_states='next_steps', message_types=message_types.Text)
def admin_dashboard(bot, update, state):
    chat_id = update.get_chat().get_id()
    text = update.get_message().get_text()
    if text == 'Visit admin webpage':
        bot.sendMessage(chat_id, "Dashboard")
        bot.sendMessage(
            chat_id,
            text='Click this butto to surf to the admin site',
            reply_markup=InlineKeyboardMarkup.a(
                inline_keyboard=[
                    [
                        InlineKeyboardButton.a('Admin Page', url='https://dave94.pythonanywhere.com/admin'),

                    ]
                ]
            )
        )

    if text == 'View pending orders':
        my_rest = Restaurant.objects.get(name = state.get_memory()['rest'])
        orders = my_rest.order_set.all()
        for order in orders:
            text = f"Order By: {order.order_by.first_name}\n Item: {order.item}\n Quantity: {order.quantity}"
            bot.sendMessage(
            chat_id,
            text=text,
            reply_markup=InlineKeyboardMarkup.a(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton.a('Accept', callback_data='some_callback_data'),
                            InlineKeyboardButton.a('Decline', callback_data='some_callback_data')

                        ]
                    ]
                )
            )

@processor(state_manager, from_states=state_types.All, update_types=[update_types.CallbackQuery])
def handle_callback_query(bot: TelegramBot, update, state):
    callback_data = update.get_callback_query().get_data()
    bot.answerCallbackQuery(update.get_callback_query().get_id(), text='Callback data received: {}'.format(callback_data))


