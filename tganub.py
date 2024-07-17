Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import subprocess
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Функция для выполнения Anub.py с цифрой
def run_anub_script(digit):
    result = subprocess.run(['python', 'Anub.py', digit], capture_output=True, text=True)
    return result.stdout.strip()

# Функция для создания клавиатуры с кнопками
def create_keyboard():
    keyboard = [
        [InlineKeyboardButton(str(i), callback_data=str(i)) for i in range(1, 12)],
        [InlineKeyboardButton(str(i), callback_data=str(i)) for i in range(12, 23)]
    ]
    return InlineKeyboardMarkup(keyboard)

# Обработчик команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Please choose a number:', reply_markup=create_keyboard())

# Обработчик нажатий на кнопки
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    digit = query.data
    result = run_anub_script(digit)
    query.edit_message_text(text=f"Result for {digit}:\n{result}")

def main() -> None:
    # Вставьте сюда токен вашего бота
    updater = Updater(7422393988:AAG4VeTdo4EaO5fxxulhO8nm6Ygom09_048)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
