from django_tgbot.decorators import processor
from django_tgbot.state_manager import message_types, update_types, state_types
from django_tgbot.types.update import Update
from django_tgbot.types.replykeyboardmarkup import ReplyKeyboardMarkup
from django_tgbot.types.keyboardbutton import KeyboardButton
from django_tgbot.types.replykeyboardremove import ReplyKeyboardRemove
from .bot import state_manager, TelegramBot
from .models import TelegramState, Restaurant, Order
from django_tgbot.exceptions import ProcessFailure


state_manager.set_default_update_types(update_types.Message)


@processor(state_manager, success='asked_for_rest')
def say_hello(bot: TelegramBot, update: Update, state: TelegramState):
    chat_id = update.get_chat().get_id()
    bot.sendMessage(chat_id, 'Hello there and welcome to beu delivery bot :)')
    bot.sendMessage(chat_id, 'You can search for restaurants by phone number and then again search for food items and finally submit your order!')


@processor(state_manager, from_states='asked_for_rest', success=state_types.Keep, exclude_message_types=message_types.Text)
def text_only(bot, update, state):
    bot.sendMessage(update.get_chat().get_id(), 'I\'d appreciate it if you answer in text format 😅')


@processor(state_manager, from_states='asked_for_rest', message_types=message_types.Text)
def start_rest_add(bot, update, state):
    chat_id = update.get_chat().get_id()
    text = update.get_message().get_text()
    found = False
    for rest in Restaurant.objects.all():
        if text == str(rest.phone_num):
            found = True
            state.set_name('asked_for_food')
            bot.sendMessage(chat_id, 'I found the restaurant :)')
            bot.sendMessage(chat_id, f'{rest.name} :)')
            bot.sendMessage(chat_id, 'Now, input a food item :)')
            state.set_memory({
                    'rest': rest.name
                 })
            state.set_name('asked_for_food')
    if not found:
        bot.sendMessage(chat_id, 'Restaurant not found, try to input once again, correctly this time :)')


@processor(state_manager, from_states='asked_for_food', message_types=message_types.Text)
def get_food(bot: TelegramBot, update: Update, state: TelegramState):
    chat_id = update.get_chat().get_id()
    food_name = update.get_message().get_text()
    resta=Restaurant.objects.get(name=state.get_memory()['rest'])
    found = False
    for food in resta.food_set.all():
        if food_name.lower() == food.name.lower():
            found = True
            state.set_memory({
                    'rest': state.get_memory()['rest'],
                    'item': food_name
                 })
            state.set_name('asked_for_quantity')
            bot.sendMessage(chat_id, 'Well done :)')
            bot.sendMessage(chat_id, f'How many pieces of {food.name} do you need ? :)')


    if not found:
        rnm = state.get_memory()['rest']
        bot.sendMessage(chat_id, f'No  {food_name} in {rnm}!!!')

@processor(state_manager, from_states='asked_for_quantity', message_types=message_types.Text)
def get_quantity(bot, update, state):
    chat_id = update.get_chat().get_id()
    quan = update.get_message().get_text()

    if quan.isdigit():
        bot.sendMessage(chat_id, 'Good job Hit the order button in the keybord below :)')
        bot.sendMessage(chat_id, 'Hit the Order now button below :)', reply_markup=ReplyKeyboardMarkup.a(keyboard=[
            [KeyboardButton.a(text='Order Now')]
        ]))
        state.set_memory({
                    'rest': state.get_memory()['rest'],
                    'item': state.get_memory()['item'],
                    'quan': quan
                 })
        state.set_name('order')

    else:
        bot.sendMessage(chat_id, 'Enter numbers only!')

@processor(state_manager, from_states='order', fail=state_types.Keep, message_types=message_types.Text)
def send_order(bot, update, state):
    chat_id = update.get_chat().get_id()
    text = update.get_message().get_text()
    user = state.telegram_user
    rest = Restaurant.objects.get(name = state.get_memory()['rest'])
    if text == 'Order Now':
        Order.objects.create(order_by = user,
                item = state.get_memory()['item'],
                quantity = state.get_memory()['quan'],
                restaurant = rest
            )
        state.set_memory({
                    'rest': state.get_memory()['rest'],
                    'item': state.get_memory()['item'],
                    'quan': state.get_memory()['quan'],
                    'user_from_object': user.username,
                    'rest_name_': rest.name,
                    'object_created': "Yes"
                 })
        bot.sendMessage(chat_id, "You're done, your order have been submitted!", reply_markup=ReplyKeyboardRemove.a(remove_keyboard=True))
        bot.sendMessage(chat_id, "You can order again by searching for a restaurant", reply_markup=ReplyKeyboardRemove.a(remove_keyboard=True))
        state.set_name('asked_for_rest')




