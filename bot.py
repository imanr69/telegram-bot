from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# توکن ربات که از BotFather گرفتی
TOKEN = "8064833361:AAHCriDXzPZXEVil6P9xzcN0oi7zU0YXPuI"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! 🎉 ربات من فعاله.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("دستورهای موجود:\n/start\n/help")

def main():
    # ساخت اپلیکیشن ربات
    application = ApplicationBuilder().token(TOKEN).build()

    # ثبت هندلرها (دستورات)
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    print("ربات روشن شد روی Render ...")
    # این تابع لوپ asyncio رو خودش مدیریت می‌کنه و ربات رو روشن نگه می‌داره
    application.run_polling()

if __name__ == "__main__":
    main()
