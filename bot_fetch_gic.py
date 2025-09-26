import os
import logging
import requests
import sqlite3
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from cryptography.fernet import Fernet

# ===== Config =====
TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY", Fernet.generate_key().decode())
fernet = Fernet(SECRET_KEY.encode())

PORT = int(os.environ.get("PORT", 8443))
WEBHOOK_URL = os.environ.get("RENDER_EXTERNAL_URL")

# ===== Database =====
DB_PATH = "accounts.db"
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS accounts (id INTEGER PRIMARY KEY, user TEXT, password TEXT)")
conn.commit()
conn.close()

# ===== Flask (Render healthcheck) =====
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Bot is running."

# ===== Telegram Handlers =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Xin chào! Bot GIC Portal đã sẵn sàng.")

async def setaccount(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 2:
        await update.message.reply_text("Dùng: /setaccount user pass")
        return
    user, pw = context.args
    enc_pw = fernet.encrypt(pw.encode()).decode()
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM accounts")
    c.execute("INSERT INTO accounts (user, password) VALUES (?,?)", (user, enc_pw))
    conn.commit()
    conn.close()
    await update.message.reply_text("✅ Đã lưu tài khoản.")

async def portal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT user,password FROM accounts LIMIT 1")
    row = c.fetchone()
    conn.close()
    if not row:
        await update.message.reply_text("⚠️ Chưa có tài khoản. Dùng /setaccount trước.")
        return
    user, enc_pw = row
    pw = fernet.decrypt(enc_pw.encode()).decode()
    # Fake request tới portal (demo)
    await update.message.reply_text(f"🔑 Đăng nhập {user}@portal.gic.vn bằng password {pw[:2]}*** thành công (demo).")

def main():
    app = ApplicationBuilder().token(TELEGRAM_API_KEY).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("setaccount", setaccount))
    app.add_handler(CommandHandler("portal", portal))

    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TELEGRAM_API_KEY,
        webhook_url=f"{WEBHOOK_URL}/{TELEGRAM_API_KEY}"
    )

if __name__ == "__main__":
    main()
