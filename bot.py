from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ✅ Your bot token (embedded directly)
BOT_TOKEN = "7707396854:AAGNdmGNqdu4WvSEKMOWG-mQH3ft2Gm17tI"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! I'm your bot. How can I help you?")

# /hello command
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Hello, {update.effective_user.first_name}!")

# Entry point
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("hello", hello))

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
