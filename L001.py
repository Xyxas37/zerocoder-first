import telebot

# Замените 'YOUR_BOT_TOKEN' на токен, который вы получили от BotFather
TOKEN = '8119696286:AAFwTu4gmQhtkwQut60R2ewB4pU_gthD8jc'
bot = telebot.TeleBot(TOKEN)

# Обработчик для приёма текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, "этот бот лежит на локальном сервере")

# Запуск бота
bot.polling()