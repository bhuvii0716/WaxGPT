from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import openai
import os
from pyrogram import enums

model_engine = "text-davinci-003"

API_HASH1 = os.environ["API_HASH"],
bot_token1 = os.environ["BOT_TOKEN"]

bot = Client("DumperGPT", api_id=3769190, api_hash=API_HASH1, bot_token=bot_token1)

START_BUTTON = JOIN_BUTTON = InlineKeyboardMarkup([[InlineKeyboardButton("Channel", url="https://t.me/DumperBots")], [InlineKeyboardButton("Help", callback_data="help")], [InlineKeyboardButton("Back", callback_data="back")]])
JOIN_BUTTON = InlineKeyboardMarkup([[InlineKeyboardButton("Channel", url="https://t.me/DumperBots")], [InlineKeyboardButton("Joined", callback_data="chatgpt")]])

@bot.on_message(filters.command("start") & filters.all)
async def start(bot, msg):
    reply_markup = START_BUTTON
    await msg.reply_text(text="<b>𝖧𝖾𝗅𝗅𝗈 𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝗍𝗈 𝖣𝗎𝗆𝗉𝖾𝗋𝖦𝖯𝖳 𝖡𝗈𝗍. 𝖳𝗁𝗂𝗌 𝖻𝗈𝗍 𝗉𝗋𝗈𝗏𝗂𝖽𝖾 𝖢𝗁𝖺𝗍𝖦𝖯𝖳 & 𝖳𝖾𝗑𝗍 𝗍𝗈 𝖨𝗆𝖺𝗀𝖾 𝖲𝖾𝗋𝗏𝗂𝖼𝖾𝗌.\n\n𝖲𝖾𝗅𝖾𝖼𝗍 𝖺 𝖲𝖾𝗋𝗏𝗂𝖼𝖾 𝖿𝗋𝗈𝗆 𝖻𝖾𝗅𝗈𝗐 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌\n\n𝖠 𝖯𝗋𝗈𝖽𝗎𝖼𝗍 𝗈𝖿 @TheDumperNetwork</b>", reply_markup=reply_markup)
    await msg.reply_text("<b>Use /ask For ChatGPT Questions</b>")

@bot.on_callback_query()
def callback_query(bot, CallBackQuery):
    reply_markup = START_BUTTON
    if CallBackQuery.data == "help":
        text = """
        <b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 :\n/ask <q> - For chatGPT Questions\n\n𝖤𝗑𝖺𝗆𝗉𝗅𝖾 :\n/ask what's 138 times 4</b>
        """
        CallBackQuery.edit_message_text(text, reply_markup=reply_markup)
    elif CallBackQuery.data == "source":
        text = "<b>𝖨𝖿 𝗒𝗈𝗎 𝗐𝖺𝗇𝗍 𝗍𝗁𝗂𝗌 𝖻𝗈𝗍'𝗌 𝗌𝗈𝗎𝗋𝖼𝖾 𝖼𝗈𝖽𝖾\n\n𝖢𝗈𝗇𝗍𝖺𝖼𝗍 : @Walker_web</b>"
        CallBackQuery.edit_message_text(text, reply_markup=reply_markup)
    elif CallBackQuery.data == "back":
        text = "<b>𝖧𝖾𝗅𝗅𝗈 𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝗍𝗈 𝖣𝗎𝗆𝗉𝖾𝗋𝖦𝖯𝖳 𝖡𝗈𝗍. 𝖳𝗁𝗂𝗌 𝖻𝗈𝗍 𝗉𝗋𝗈𝗏𝗂𝖽𝖾 𝖢𝗁𝖺𝗍𝖦𝖯𝖳 & 𝖳𝖾𝗑𝗍 𝗍𝗈 𝖨𝗆𝖺𝗀𝖾 𝖲𝖾𝗋𝗏𝗂𝖼𝖾𝗌.\n\n𝖲𝖾𝗅𝖾𝖼𝗍 𝖺 𝖲𝖾𝗋𝗏𝗂𝖼𝖾 𝖿𝗋𝗈𝗆 𝖻𝖾𝗅𝗈𝗐 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌\n\n𝖠 𝖯𝗋𝗈𝖽𝗎𝖼𝗍 𝗈𝖿 @TheDumperNetwork</b>"
        CallBackQuery.edit_message_text(text, reply_markup=reply_markup)


@bot.on_message(filters.command("ask") & filters.all)
async def chatgpt(bot, msg):
    api = await bot.get_messages("-1001892032949", 2)
    openai.api_key = api.text
    try:
        member = await bot.get_chat_member("DumperBots", msg.from_user.id)
        is_mem = True
    except UserNotParticipant:
        reply_markup = JOIN_BUTTON
        await msg.reply_text(text="<b>𝖸𝗈𝗎 𝗆𝗎𝗌𝗍 𝗃𝗈𝗂𝗇 𝗈𝗎𝗋 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 𝗍𝗈 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝗌𝖾𝗋𝗏𝗂𝖼𝖾</b>", reply_markup=reply_markup)
        return

    if is_mem:
        prompt = msg.text.replace("/ask ", "")
        await bot.send_chat_action(msg.chat.id, enums.ChatAction.TYPING)

        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,)

        response = completion.choices[0].text
        await msg.reply_text(response)
       
if __name__ == "__main__":
    print("Bot is Running")
    bot.run()
