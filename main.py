import telebot
from telebot import types
import time
import threading
import os
from keep_alive import keep_alive
from flask import Flask, request

BOT_TOKEN = 8325375868:AAEAvYZK_QqdYiF8R3ilgRdKRuXBzEwO78Y

if not BOT_TOKEN:
    print("❌ ERROR: BOT_TOKEN not found in environment variables!")
    print("Please add your bot token in the Secrets tab.")
    exit(1)

bot = telebot.TeleBot(BOT_TOKEN)

repeat_active = False
repeat_message = ""
repeat_chat_id = 0

active_users = set()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    active_users.add(message.chat.id)
    text = (
        "💎 *Welcome to the Official MoneyMatrix Bot!* 💎\n\n"
        "🏦 Corporate bank account chahiye? 🔥\n"
        "⚡ Best deals, instant setup & VIP benefits ke liye abhi join karo 👇\n\n"
        "👉 [Join Our Official Channel](https://t.me/MoneyMatrix_Biz)\n\n"
        "💬 Stay connected for exclusive offers and latest updates!"
    )
    bot.send_message(message.chat.id, text, parse_mode='Markdown')

@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    active_users.add(message.chat.id)
    for user in message.new_chat_members:
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("1️⃣ Account hai", callback_data="option_account")
        btn2 = types.InlineKeyboardButton("2️⃣ Panel hai", callback_data="option_panel")
        btn3 = types.InlineKeyboardButton("3️⃣ Mediator hu", callback_data="option_mediator")
        btn4 = types.InlineKeyboardButton("4️⃣ Inme se koi nahi", callback_data="option_none")
        markup.add(btn1, btn2, btn3, btn4)
        
        welcome_text = (
            f"👋 Welcome {user.first_name}!\n\n"
            "Kya tumhare paas account ya panel hai ya tum mediator ho?\n\n"
            "👇 Choose your option:"
        )
        bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("option_"))
def handle_option_selection(call):
    user_mention = f"@{call.from_user.username}" if call.from_user.username else call.from_user.first_name
    user_id = call.from_user.id
    
    responses = {
    "option_holder": (
        f"🎯 {user_mention} (ID: {user_id})\n\n"
        "💎 VIP Account Service — Contact: @Ghost_Commander\n\n"
        "📋 *Provide Account Details in Safe Format:*\n"
        "• Account Name: <Alias>\n"
        "• Bank Name: <Bank>\n"
        "• Limit: <Daily/Monthly Limit>\n"
        "• Account Type: <Current/Savings>\n"
        "• Availability: <Yes/No>\n"
        "• Contact (Telegram): @your_username\n"
        "• Notes: <Extra info / verified status>\n\n"
        "🚫 *Do not share sensitive info like PIN, full A/C no, passwords, Aadhaar, or PAN publicly.*\n"
        "🔒 For verified & private checks, DM @Ghost_Commander."
    ),
    
    "option_panel": (
        f"🎯 {user_mention} (ID: {user_id})\n\n"
        "🔧 Panel Service — Contact: @Ghost_Commander\n\n"
        "📋 *Provide Panel Details:*\n"
        "• Panel Name / Brand: <Name>\n"
        "• Features: <List Features>\n"
        "• Access Type: <Web/App>\n"
        "• Price / Rent: <Amount>\n"
        "• Availability: <Yes/No>\n"
        "• Contact (Telegram): @your_username\n"
        "• Notes: <Demo/Verification Info>\n\n"
        "⚠️ *Never post login credentials or admin passwords publicly.*\n"
        "🔒 Verified access process — DM @Ghost_Commander."
    ),
    
    "option_mediator": (
        f"🎯 {user_mention} (ID: {user_id})\n\n"
        "🤝 Mediator Service — Contact: @Ghost_Commander\n\n"
        "📋 *Mediator Info:*\n"
        "• Mediator Name / Alias: <Name>\n"
        "• Region / City: <Location>\n"
        "• Commission: <Percentage / Fixed>\n"
        "• Services: <What you handle>\n"
        "• Contact (Telegram): @your_username\n"
        "• Notes: <Preferred mode / trust level>\n\n"
        "💬 Ek pyar bhara aur dangerous message ❤️⚠️:\n"
        "👉 Scam mat karo mere kisi bhi member ke sath 🙏\n"
        "👉 Aap bhi kamao aur dusron ko bhi kamane do 💸\n"
        "Safe aur verified deal hi karo 🔐"
    ),
    
    "option_none": (
        f"✅ Thanks {user_mention}!\n\n"
        "📢 Aap hamare channel me active reh sakte ho updates ke liye:\n"
        "👉 @MoneyMatrix_Biz"
    )
}
    
    response_text = responses.get(call.data, "❌ Invalid option")
    bot.answer_callback_query(call.id)
    
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)
    except:
        pass
    
    bot.send_message(call.message.chat.id, response_text)

@bot.message_handler(commands=['adduser'])
def add_user(message):
    active_users.add(message.chat.id)
    bot.reply_to(message, "👑 User added successfully to MoneyMatrix Network!")

@bot.message_handler(commands=['repeat'])
def start_repeating(message):
    global repeat_active, repeat_message, repeat_chat_id
    repeat_message = message.text.replace('/repeat', '').strip()
    
    if not repeat_message:
        bot.reply_to(message, "❌ Error: Please provide a message to repeat.\nUsage: /repeat Your message here")
        return
    
    repeat_chat_id = message.chat.id
    repeat_active = True
    bot.reply_to(message, "✅ Auto-message started. Message har 1 minute me bheja jayega.")

    def repeat_func():
        error_count = 0
        while repeat_active:
            try:
                bot.send_message(repeat_chat_id, repeat_message)
                error_count = 0
            except Exception as e:
                error_count += 1
                print(f"Error sending repeat message: {e}")
                if error_count >= 5:
                    print("Too many errors, stopping repeat")
                    try:
                        bot.send_message(repeat_chat_id, "🛑 Auto-message stopped due to errors.")
                    except:
                        pass
                    break
            time.sleep(60)

    threading.Thread(target=repeat_func, daemon=True).start()

@bot.message_handler(commands=['stoprepeat'])
def stop_repeating(message):
    global repeat_active
    repeat_active = False
    bot.reply_to(message, "🛑 Auto-message stopped.")

@bot.message_handler(commands=['whois'])
def whois(message):
    username = message.from_user.username if message.from_user.username else "No username"
    bot.reply_to(message, f"🪪 User Info:\nName: {message.from_user.first_name}\nUsername: @{username}")

@bot.message_handler(commands=['scammeralert'])
def scammer_alert(message):
    text = message.text.replace('/scammeralert', '').strip()
    
    if not text:
        bot.reply_to(message, "❌ Error: Please provide scammer details.\nUsage: /scammeralert @username or user details")
        return
    
    alert_message = (
        "🚨 <b>SCAMMER ALERT</b> 🚨\n\n"
        "⚠️ WARNING: Potential scammer detected!\n\n"
        f"📍 Details: {text}\n\n"
        "❌ DO NOT DEAL with this person!\n"
        "✅ Only trust verified members\n"
        "💎 Safe deals ke liye @Ghost_Commander se contact karo\n\n"
        "🔒 Stay Safe! Stay Smart!"
    )
    
    bot.send_message(message.chat.id, alert_message, parse_mode='HTML')
    
    if active_users and len(active_users) > 1:
        success = 0
        for chat_id in active_users:
            if chat_id != message.chat.id:
                try:
                    bot.send_message(chat_id, alert_message, parse_mode='HTML')
                    success += 1
                except:
                    pass
        
        if success > 0:
            bot.reply_to(message, f"✅ Alert sent to {success} users!")

@bot.message_handler(commands=['broadcast'])
def broadcast(message):
    text = message.text.replace('/broadcast', '').strip()
    
    if not text:
        bot.reply_to(message, "❌ Error: Please provide a message to broadcast.\nUsage: /broadcast Your message here")
        return
    
    if not active_users:
        bot.reply_to(message, "⚠️ No active users to broadcast to.")
        return
    
    success_count = 0
    fail_count = 0
    
    for chat_id in active_users:
        try:
            bot.send_message(chat_id, f"📢 Broadcast:\n{text}")
            success_count += 1
        except Exception as e:
            fail_count += 1
            print(f"Failed to send broadcast to {chat_id}: {e}")
    
    bot.reply_to(message, f"📢 Broadcast sent!\n✅ Successful: {success_count}\n❌ Failed: {fail_count}")

@bot.message_handler(func=lambda message: message.text and 'account' in message.text.lower())
def handle_account_message(message):
    active_users.add(message.chat.id)
    user_mention = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
    user_id = message.from_user.id
    
    response = (
        f"🎯 {user_mention} (ID: {user_id})\n\n"
        "💎 VIP Account service ke liye please contact karo:\n"
        "👉 @Ghost_Commander\n\n"
        "🔥 Best deals aur instant setup ke liye DM karo!"
    )
    bot.reply_to(message, response)

@bot.message_handler(func=lambda message: True)
def track_users(message):
    active_users.add(message.chat.id)

if __name__ == "__main__":
    keep_alive()
    print("✅ MoneyMatrix Bot is Running...")
    
    bot.remove_webhook()
    time.sleep(1)
    
    try:
        bot.infinity_polling(timeout=60, long_polling_timeout=60, skip_pending=True)
    except Exception as e:
        print(f"Polling error: {e}")
        print("Retrying in 5 seconds...")
        time.sleep(5)
        bot.infinity_polling(timeout=60, long_polling_timeout=60, skip_pending=True)
        
