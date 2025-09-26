# GIC Telegram Bot (SQLite + Webhook Render)

## 1. Chuẩn bị
- Tạo bot trên Telegram bằng **@BotFather**, lấy `TELEGRAM_API_KEY`.
- Chuẩn bị `SECRET_KEY` để mã hoá password (có thể để auto-generate).

## 2. Source code gồm
- `bot_fetch_gic.py` (bot chính)
- `requirements.txt`
- `Dockerfile`
- `README.md`

## 3. Deploy trên Render
1. Tạo **Web Service** chọn Docker.
2. Upload toàn bộ source.
3. Thiết lập **Environment Variables**:
   - `TELEGRAM_API_KEY`: API key từ BotFather.
   - `RENDER_EXTERNAL_URL`: URL Render (ví dụ `https://mybot.onrender.com`).
   - `SECRET_KEY`: (tuỳ chọn) chuỗi bí mật để mã hoá password.

## 4. Command Bot
