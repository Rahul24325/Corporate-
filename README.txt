==========================================
  MoneyMatrix Telegram Bot - Setup Guide
==========================================

Created by: Rahul
Bot Features: Welcome messages, Interactive buttons, Auto-repeat, Broadcast, User tracking

==========================================
FILES INCLUDED:
==========================================
1. main.py - Main bot code with all handlers
2. keep_alive.py - Flask server to keep bot alive 24/7
3. replit.md - Complete documentation
4. .gitignore - Git ignore file
5. pyproject.toml - Python dependencies

==========================================
REQUIREMENTS:
==========================================
- Python 3.11+
- pyTelegramBotAPI (telebot)
- Flask

==========================================
SETUP INSTRUCTIONS:
==========================================

1. GET BOT TOKEN:
   - Open Telegram and search for @BotFather
   - Send /newbot command
   - Follow instructions to create your bot
   - Copy the bot token (looks like: 1234567890:ABCdefGHIjklMNOpqrsTUVwxyz)

2. INSTALL DEPENDENCIES:
   Run: pip install pyTelegramBotAPI flask

3. SET BOT TOKEN:
   - Create environment variable: BOT_TOKEN="your_bot_token_here"
   - Or edit main.py and replace os.environ.get('BOT_TOKEN') with your token

4. RUN THE BOT:
   Run: python main.py

==========================================
BOT COMMANDS:
==========================================
/start - Welcome message
/repeat [message] - Auto-send message every minute
/stoprepeat - Stop auto-messaging
/broadcast [message] - Send to all users
/scammeralert [details] - Send scammer warning to all users
/adduser - Add user to network
/whois - Get user info

==========================================
FEATURES:
==========================================
✅ Interactive buttons for new members (auto-delete after click)
✅ Auto-contact when "account" mentioned
✅ Scammer alert system - warn all users
✅ Broadcast to all active users
✅ Auto-repeat messaging
✅ User tracking system
✅ Error handling with auto-recovery
✅ Clean interface - welcome messages auto-delete

==========================================
CONTACT:
==========================================
For VIP services: @Ghost_Commander
Channel: @MoneyMatrix_Biz

==========================================
