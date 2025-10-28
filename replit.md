# MoneyMatrix Telegram Bot

## Overview
MoneyMatrix Bot is a Telegram bot designed for managing a business network focused on corporate bank accounts. The bot provides automated messaging, user management, and broadcasting features.

## Features
- **Welcome Message**: Greets new users with information about MoneyMatrix services
- **New Member Welcome with Buttons**: Automatically welcomes new group members with interactive buttons to select their role (Account holder, Panel owner, Mediator) - **message auto-deletes after selection**
- **Auto-Contact Handler**: When users mention "account", bot automatically replies with their info and directs them to @Ghost_Commander
- **Scammer Alert System**: `/scammeralert` command to warn all users about potential scammers
- **Auto-Repeat Messaging**: Send messages automatically every minute with `/repeat` command
- **User Lookup**: Get user information with `/whois` command
- **Broadcasting**: Send announcements to all active users with `/broadcast`
- **User Management**: Add users to the network with `/adduser`

## Commands
- `/start` - Display welcome message with channel link
- `/adduser` - Add a user to MoneyMatrix Network
- `/repeat [message]` - Start auto-repeating a message every minute
- `/stoprepeat` - Stop the auto-repeat feature
- `/whois` - Display user information
- `/broadcast [message]` - Broadcast a message to all users
- `/scammeralert [details]` - Send scammer warning alert to all users

## Project Structure
- `main.py` - Main bot file with all command handlers
- `keep_alive.py` - Flask web server to keep bot running on Replit
- `.gitignore` - Python project gitignore

## Environment Variables
- `BOT_TOKEN` - Your Telegram bot token from @BotFather (stored in Replit Secrets)

## How It Works
1. The bot uses pyTelegramBotAPI library to interact with Telegram
2. A Flask web server runs on port 5000 to keep the bot alive
3. The repeat feature uses threading to send messages every 60 seconds with error handling
4. All sensitive data (bot token) is stored securely in environment variables
5. Active users are tracked in memory for broadcast functionality
6. Input validation prevents empty messages in repeat and broadcast commands

## Recent Changes
- **October 28, 2025**: Initial setup with all core features implemented
  - Created bot with all command handlers
  - Added keep-alive Flask server
  - Configured environment variables for secure token storage
  - Set up Python 3.11 with required dependencies
  - Implemented user tracking system for broadcast functionality
  - Added input validation for /repeat and /broadcast commands
  - Enhanced error handling with auto-stop after 5 consecutive errors
  - Added success/failure reporting for broadcasts
  - **Added interactive inline buttons** for new member welcome (4 options)
  - **Added callback handlers** for button clicks with personalized responses
  - **Fixed Error 409** by implementing skip_pending and webhook removal
  - Added auto-contact feature for "account" keyword mentions
  - **Auto-delete welcome messages** after user selects option (clean interface)
  - **Added /scammeralert command** to warn all users about potential scammers

## User Preferences
None specified yet.

## Technology Stack
- Python 3.11
- pyTelegramBotAPI (telebot)
- Flask
- Threading for auto-repeat functionality
