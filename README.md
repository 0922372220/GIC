# GIC Portal Bot

## Cấu hình ENV
- TELEGRAM_API_KEY: token BotFather
- SECRET_KEY: key để mã hoá mật khẩu
- RENDER_EXTERNAL_URL: URL service Render

## Deploy Render
1. Tạo dịch vụ Web Service, chọn Docker.
2. Upload source gồm:
   - bot_fetch_gic.py
   - requirements.txt
   - Dockerfile
   - README.md
3. Set ENV trong Render dashboard.
4. Deploy.

## Lệnh trong Telegram
- /start → khởi động bot
- /setaccount user pass → lưu tài khoản (mật khẩu mã hoá)
- /portal → đăng nhập portal.gic.vn (demo)
