from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from googletrans import Translator

translator = Translator()

async def auto_translate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    try:
        result = translator.translate(text, src='zh-cn', dest='vi')
        await update.message.reply_text(result.text)
    except:
        await update.message.reply_text("❌ Lỗi dịch!")

app = ApplicationBuilder().token("7738046068:AAG1s3ppMghwyEvbMgLwSKMMnLy_Sl-_S7Y").build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_translate))

print("Bot đang chạy...")
app.run_polling()