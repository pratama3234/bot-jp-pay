import telebot

TOKEN="8935537318:AAE3GnKpyrWeoRdL0gHvkjk4anx1lnARIY0"
bot=telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    text="""If I am offline on Telegram, please add me as a contact: @JP_PAY158
If you are looking to sell USDT, please follow our company's Telegram channel. This ensures you receive the latest real-time exchange rates and the most reliable trading methods. Thank you.
Our Telegram channel is: https://t.me/jppay158
Please follow us to stay connected."""
    bot.send_message(message.chat.id, text)

print("Bot JP PAY Jalan...")
bot.infinity_polling()