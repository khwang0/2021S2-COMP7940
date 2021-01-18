![](../imgs/hkbu.png)

# COM7940 Cloud Computing 

## 2020/21 S2 Lab 3 Starting a TG chatbot


| | | |
|--|--|--|
| Instructor | Dr. Kevin Wang  | kevinw@comp.hkbu.edu.hk|
| Teaching Assistant | Mr. Zijian Lei | cszjlei@comp.hkbu.edu.hk |



**Objective:**
---
Throughout this lab you will be able to:
1. Experience in running a chatbot;
2. Customize your chatbot (greeting message, issue special command);

---

<!-- adding guideline for creating and customizing chatbot. 
create something from : https://core.telegram.org/bots
-->
## 1. Installation

Install the following software on your phone:

* Telegram  

## 2.  Start a chatbot
Telegram provide an official Bots accounts that do not require additional phone number to set up. You can add @BotFather and just talk to the @BotFather follow some simple step to create  your own chatbot.

you can find more about the Telegram bot API at: https://core.telegram.org/api

###  start the chatbot and name it
Send the following massage to BotFather to create a new bot.
```cmd
/newbot
```

Then choose a user name for the bot and it should  end in 'bot'  (e.g zijianBot or zijian_bot). The BotFather will provide you a link to find your Botand a token to access the HTTP API show as the following:

```
Done! Congratulations on your new bot. You will find it at t.me/zijianTestBot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

Use this token to access the HTTP API:
1505550933:AAFlZtYKApLkUR2DNRrS95gvrCxQxeoz9Bo
Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api```
```
For example, my chatbot link is shown in the first line 

Link of my bot:  t.me/zijianTestBot  

Token of my bot : 1505550933:AAFlZtYKApLkUR2DNRrS95gvrCxQxeoz9Bo

Now the chat bot can receive your massage but can not response. You can send massage to the chatbot and the logs can see the  at the following website:

[https://api.telegram.org/bot{$token}/getUpdates](https://api.telegram.org/bot606248605:AAGv_TOJdNNMc_v3toHK_X6M-dev_1tG-JA/getUpdates) 

and change  '{$token}' to the Token of your bot.

## Preparing the development environment

Now we can try to customize our own bot to make some simple response. You need to install the following  module using

> `python-telegram-bot`: Telegram Bot API wrapper.
>
> `flask`: Web framework. Using for building webhook API.
>
> `gunicorn`: Python WSGI HTTP server for UNIX. Using for deploying web server.
>
> `requests`: HTTP client library.

```
mkdir $project_name(choose your own project name)
cd $project_name
pip install python-telegram-bot flask gunicorn requests 
#install the required module, if the pip install fails, you may update the pip version #firtst using: python -m pip install --upgrade pip
```
For security, we will using a config file to store the Token and the webhook link, first we make a config file
```
torch config.ini
```
Then we edit the config.ini as the following
```
[TELEGRAM]
ACCESS_TOKEN = {$YOUR TOKEN}
WEBHOOK_URL = {$YOUR WEBHOOK}
```
First we learn to receive massage from the telegram and echo to the massage, we will use the following API, 

> [telegram.ext.Updater]( https://python-telegram-bot.readthedocs.io/en/latest/telegram.ext.updater.html#telegram.ext.updater.Updater) : Its purpose is to receive the updates from Telegram and to deliver them to said dispatcher 

```python
import telegram
from telegram.ext import Updater,CommandHandler,MessageHandler, Filters
import configparser
import logging
def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    bot = telegram.Bot(token=(config['TELEGRAM']['ACCESS_TOKEN']))
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    #the logging helps you know when things do not work as expected
    updater = Updater(token=(config['TELEGRAM']['ACCESS_TOKEN']), use_context=True)
    dispatcher = updater.dispatcher
    updater.start_polling() # To start the bot, run:
    # print(bot.logg)
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

if __name__ == '__main__':
    main()
```





Reference:

1 python-telegram-bot official github page: https://github.com/python-telegram-bot/python-telegram-bot