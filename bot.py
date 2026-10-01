import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")
LINK_GRUP = os.getenv("LINK_GRUP")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📝 DAFTAR", callback_data="daftar")]
    ]

    await update.message.reply_text(
        "👋 Selamat datang!\n\n"
        "Tekan tombol di bawah untuk mendaftar dan mendapatkan "
        "link bergabung ke grup.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def daftar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("🔗 GABUNG GRUP", url=LINK_GRUP)]
    ]

    await query.edit_message_text(
        "✅ Pendaftaran berhasil!\n\n"
        "Silakan tekan tombol di bawah untuk bergabung ke grup.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(daftar, pattern="^daftar$"))

    print("Bot berjalan...")
    app.run_polling()


if __name__ == "__main__":
    main()
