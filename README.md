# GICore Telegram Bot

Bot Telegram để login vào GICore (claim, policyadmin, bcp) và fetch dữ liệu.

## Commands
- /setcreds user pass
- /setlinks url1 url2 url3
- /fetchnow

## Deploy trên Render
1. Upload repo có 3 file: bot_fetch_gic.py, requirements.txt, Dockerfile, README.md
2. Set env TELEGRAM_API_KEY, RENDER_EXTERNAL_URL, SECRET_KEY
3. Deploy Docker service
