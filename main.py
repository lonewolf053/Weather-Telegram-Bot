import telegram.ext as telext
from weatheralt import getweather
API_KEY = "5000501546:AAH6NP3_d08QXsi3YPk8xqxznINJF5EMBrk"

print("Bot Started...")
###Response THINGY
def sample_responses(user_inp):
  imp_msg = str(user_inp).lower()
  if imp_msg in ('hey','hi'):
    return "Howdy!!"
  elif imp_msg.split()[0] == "weather":
    return getweather(imp_msg.split()[1])

    
###MAIN THINGY
def start_command(update,context):
  update.message.reply_text('Type something to get started')

def help_commmand(update,context):
	update.message.reply_text('Type weather<space>city name to get the weather')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = sample_responses(text)
    update.message.reply_text(response)

def error(update,context):
	print(f"Update{update} cused error {context.error}")

def main():
    updater = telext.Updater(API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(telext.CommandHandler("start", start_command))
    dp.add_handler(telext.CommandHandler("help", help_commmand))
    dp.add_handler(telext.MessageHandler(telext.Filters.text,handle_message))
    dp.add_error_handler(error)

    updater.start_polling(0)
    updater.idle()

main()