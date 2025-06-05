import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import json
import os

# Настройки
BOT_TOKEN = "7692562404:AAFJ1p9BXIE4uVaU_8B-9ns4FMsU8hVXF0Y"
MEMORY_FILE = "memory.json"

# Инициализация памяти
if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "w") as f:
        json.dump({}, f)

# Загрузка памяти
def load_memory():
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

# Сохранение памяти
def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

# Команды
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я когнитивный ассистент. Напиши мне что-нибудь, и я это запомню.")

async def save_note(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.message.from_user.id)
    text = update.message.text

    memory = load_memory()
    if user_id not in memory:
        memory[user_id] = []

    memory[user_id].append(text)
    save_memory(memory)

    await update.message.reply_text("Запомнил!")

# Настройка логов
logging.basicConfig(level=logging.INFO)

# Запуск бота
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, save_note))

if name == "__main__":
    app.run_polling()
