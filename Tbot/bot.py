import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import requests

TOKEN = '8251633784:AAEV3NZ9WvJuqlxvbdwFHRJ3106xbDM0BDE'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Отправьте мне цифры — артикул Вайлдберриз, и я пришлю ссылку на него')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    product_id = update.message.text.strip()
    if product_id.isdigit():
        link = f'https://www.wildberries.ru/catalog/{product_id}/detail.aspx?targetUrl=SP'
        response = requests.get(link)
        if response.status_code != 200:
            if "не найдено" in response.text or "404" in response.text:
                await update.message.reply_text(f'Такого товара нет(((')
            else:
                await update.message.reply_text(f'Ссылка на товар: {link}')
        else:
            await update.message.reply_text('Произошла ошибка при проверке товара. Попробуйте позже')
    else:
        await update.message.reply_text('Пожалуйста, отправьте только цифры — ID товара.')


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == '__main__':
    main()