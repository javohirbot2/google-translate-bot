from telegram.ext import Updater,MessageHandler,CommandHandler,Filters
from googletrans import Translator

updater = Updater('5047160628:AAFI241gfwIu6YoT8ykd-8u3_zcrtj-AwDM',use_context = True )

def start(updater,context):
  user = updater.message.from_user
 updater.message.reply_html('👋🏻Assalomu alaykum <b>{}!</b>\n \n<b>Ushbu bot orqali matnlarni english\n uzbek tarzida tarjima qilishingiz\n mumkin. Botga matn yuboring.\n \n /start - Botni ishga tushirish.</b>')
format(user.first_name))
 
def echo(updater,context):
 usr_msg =updater.message.text
 translator = Translator()
 translation = translator.translate(usr_msg,dest='hi') 
 updater.message.reply_text(translation.text)
 
dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()
