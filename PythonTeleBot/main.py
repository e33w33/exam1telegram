import telebot
bot = telebot.TeleBot('5069065190:AAEvP1cCLnOXERmqDY9DFZeMSPHpM9aXMZY')
name = ''
complaints = ''
age = 0


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Здравствуйте, напишите свое ФИО")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    if message.text.lower() in ['привет', 'здравстуйте']:
        bot.send_message(chat_id, 'Здравствуйте, для консультации пройдите регестрацию /start')
    if message.text.lower().startswith('я'):
        # save_data()
        bot.send_message(chat_id, "Ваша заявка принята, ожидайте звонка от специалиста")
    else:
        username = message.chat.username
        bot.send_message(chat_id, f"{username}, на что жалуетесь?")


bot.infinity_polling()