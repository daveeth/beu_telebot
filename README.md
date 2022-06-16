# beu_telebot

![Screenshot for beu_telebot](https://www.pythonanywhere.com/user/dave94/files/home/dave94/mysite/media/test1.PNG)

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

Currenntly, there are two restaurants in the database identified by the numbers 0968204729 and 0930303030 respectively and they offer the following foods.

 - ### The Beu Restaurant, 0968204729

  - Pizza
  - Burger
  - Lazagna
  - ጨጨብሳ
  - Coffee

 - ### Bot Restaurant(0930303030)

  - Electron
  - Photon
  - Python

#### These restaurants are fictitious and are created initially for testing purposes and in no way represent real restaurants.

#### This is how you can test them.

##### For [beu delivery bot](https://t.me/our_beu_delivery_bot)

- Enter one of the two numbers
- The bot will identify if correct number is provided or send a message to enter the right number,
- Now, if correct number is provided, the bot sends a message and prompts as user to enter a food item, the Amharic word can also be written to get that food item,
- The food must belong in the food catalogue of the restaurant identified by the number entered previously,
- If the bot can find the food, it will prompt again for quantity,
- If a number is provided, the bot will send a successful message and an order now button is sent,
- User can now submit order with the touch or click of a button and this whole process repeats.

##### For admin bot[beu admin bot](https://t.me/beu_admin_bot)

- User must be an admin of a restaurant and the bot asks a number first to proceed for the future,
- If correct number is provided, the bot will send a set of keyboard buttons to manage orders,

#### To go beyond testing and and use the admin for your own restaurant, you must follow the following steps...

- Grab a number by sending a request to the admin of this application to create a new restaurant identified by your number,
- To contact admin, [ click here](https://t.me/Daw_94),


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
