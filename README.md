# beu_telebot
A fully functional telegram bot for users to order food, and for restaurants to track orders

This project is aimed at developing a simple-to-use telegram bot for delivery systems to reduce much of the heavy 
lifting required to keep track of orders and users.


Two bots drive the engine of this telebot application

  - [beu bot](https://t.me/our_beu_delivery_bot)
  - [beu admin bot](https://t.me/beu_admin_bot)
  
At first, nearly anyone who knows the links to th two bots can gain access to both of them. Telegram bot APIs use TelegramStates to transition   
between several states that exist inherently between a user and a bot. So, th bot asks a totally different question with varying response when    
a user encounters for the first time and anytime afterwards.

The first bot is recommended to be publicly availabel, and user can be asked questions about a restaurant and the food items in it...    
Every restaurant is identified by a phone number with the exact pattern of 09########,with no spaces where # is meant to represent any number.        
After the right number is received, the user will be prompted to enter a food item, and the bot hooks into the database to retrive details as required     
and the process goes on and on...

The second bot, however, is only for admin and owners of restaurants where they can see details of orders submitted by all users. Any user who does not
know the number used to identify restaurants can not gain access to the full functionality of the bot.
  

## Frameworks used

beu_telebot is programmed with Django on top of python
  
### For the backend

#### The bot uses Django web framework installed on a linux server provided by pythonanywhere

#### The SQLite database was also used to hold all data ranging from users to chat, states and application-specific models

### For the bot processor

#### django-tgbot handles all the logic related to state and chat management

### For the web frontend

#### The Django template engine is by far a relief when it comes to faster and easier interaction between backend and frontend

### Here are the links for the two bots
 - ## [beu_delivery_bot](https://t.me/our_beu_delivery_bot)
 - ## [beu admin bot](https://t.me/beu_admin_bot)
