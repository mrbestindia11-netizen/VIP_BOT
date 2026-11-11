import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "9264862421:AAF63XT5f9UfHHDOeOsRYF9fNEHPfY9Az_s"
bot = telebot.TeleBot(TOKEN)

ADMIN_USERNAME = "@TYSON_RAY"

# ✅ NORMAL CHANNEL
NORMAL_LINK = "https://t.me/+5RILRXGY_zM1YTM1"
NORMAL_ID = -1002488631823

# ✅ VIP CHANNEL
VIP_LINK = "https://t.me/+05SleR9r23swYzA1"
VIP_ID = -1003939671132

# VIP GROUP LINK - Join ke baad jo milega
VIP_GROUP_LINK = "https://t.me/+05SleR9r23swYzA1"

def check_join(user_id):
    try:
        m1 = bot.get_chat_member(NORMAL_ID, user_id)
        m2 = bot.get_chat_member(VIP_ID, user_id)
        if m1.status in ["left", "kicked"] or m2.status in ["left", "kicked"]:
            return False
        return True
    except Exception as e:
        print(e)
        return False

@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.first_name
    if not check_join(message.from_user.id):
        text = f"""
👋 𝐇𝐄𝐋𝐋𝐎 {name} 🔥

💎 𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗧𝗢 𝗢𝗨𝗥 𝗩𝗜𝗣 𝗖𝗢𝗠𝗠𝗨𝗡𝗜𝗧𝗬 💎

Ab se LOSS kya hota hai bhul jao 😎
Ab profit hi profit hoga 🚀

👇 𝐍𝐈𝐂𝐇𝐄 𝐃𝐈𝐘𝐄 𝐃𝐎𝐍𝐎 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐊𝐎 𝐉𝐎𝐈𝐍 𝐊𝐀𝐑𝐋𝐎 👇
Aur FREE me VIP GROUP ka link pao 🎁

━━━━━━━━━━━━━━━
💬 𝐀𝐀𝐏𝐊𝐀 𝐉𝐈𝐓𝐍𝐀 𝐁𝐇𝐈 𝐋𝐎𝐒𝐒 𝐇𝐀𝐈,
𝐇𝐀𝐌𝐄 𝐁𝐎𝐋𝐎 𝐁𝐑𝐎𝐓𝐇𝐄𝐑 ❤️
𝐑𝐄𝐂𝐎𝐕𝐄𝐑 𝐀𝐑𝐀𝐌 𝐒𝐄 𝐇𝐎 𝐉𝐀𝐘𝐄𝐆𝐀 ✅

📩 Contact: {ADMIN_USERNAME}
━━━━━━━━━━━━━━━
"""
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("📢 JOIN NORMAL CHANNEL 📢", url=NORMAL_LINK))
        markup.add(InlineKeyboardButton("👑 JOIN VIP CHANNEL 👑", url=VIP_LINK))
        markup.add(InlineKeyboardButton("✅ CHECK JOIN - VERIFY KARO", callback_data="check"))
        bot.send_message(message.chat.id, text, reply_markup=markup)
    else:
        send_vip(message.chat.id, name)

def send_vip(chat_id, name):
    vip_text = f"""
🎉 𝐂𝐎𝐍𝐆𝐑𝐀𝐓𝐔𝐋𝐀𝐓𝐈𝐎𝐍𝐒 𝐁𝐑𝐎 {name} 🎉

👑 𝐋𝐎 𝐀𝐏𝐊𝐀 𝐕𝐈𝐏 𝐅𝐑𝐄𝐄 𝐆𝐑𝐎𝐔𝐏 𝐋𝐈𝐍𝐊 👑

🔥 Ab aap hamari VIP Family ka hissa ho 🔥
💎 Daily VIP Updates
💎 Full Support
💎 Loss Recovery Plan

👇 𝐍𝐈𝐂𝐇𝐄 𝐂𝐋𝐈𝐂𝐊 𝐊𝐀𝐑𝐊𝐄 𝐉𝐎𝐈𝐍 𝐊𝐀𝐑𝐎 👇
"""
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🚀 JOIN VIP FREE GROUP 🚀", url=VIP_GROUP_LINK))
    markup.add(InlineKeyboardButton("📩 ADMIN SE BAAT KARO", url="https://t.me/TYSON_RAY"))
    bot.send_message(chat_id, vip_text, reply_markup=markup)

@bot.callback_query_handler(func=lambda c: c.data == "check")
def check(call):
    if check_join(call.from_user.id):
        send_vip(call.message.chat.id, call.from_user.first_name)
    else:
        bot.answer_callback_query(call.id, "❌ Bhai pehle DONO channel join karo!", show_alert=True)

print("Bot Started...")
bot.polling()
