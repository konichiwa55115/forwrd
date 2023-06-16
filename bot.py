import telegram

# Replace YOUR_TOKEN with your Telegram bot token
bot = telegram.Bot(token='YOUR_TOKEN')

# Replace YOUR_CHAT_ID with your Telegram chat ID
chat_id = 6234365091

def forward_message(update, context):
    message = update.message
    # Forward the message to your chat ID
    bot.forward_message(chat_id=chat_id, from_chat_id=message.chat_id, message_id=message.message_id)

# Register the forward_message function as a handler for all messages
updater = telegram.Updater(token='YOUR_TOKEN', use_context=True)
updater.dispatcher.add_handler(telegram.MessageHandler(telegram.Filters.all, forward_message))
updater.start_polling()
updater.idle()
