from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import openai
from pyrogram import enums
from os import environ

openai.api_key = "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"

model_engine = "text-davinci-003"

bot = Client("DumperGPT", api_id=int(environ["API_ID"]), api_hash=environ["API_HASH"], bot_token="6247526690:AAGfFoP0l6nXpr5NNqI9I-BMKSR9ffQ3aMU")

START_BUTTON = JOIN_BUTTON = InlineKeyboardMarkup([[InlineKeyboardButton("Channel", url="https://t.me/DumperBots")], [InlineKeyboardButton("Help", callback_data="help")], [InlineKeyboardButton("Source code", callback_data="source")], [InlineKeyboardButton("Back", callback_data="back")]])
JOIN_BUTTON = InlineKeyboardMarkup([[InlineKeyboardButton("Channel", url="https://t.me/DumperBots")], [InlineKeyboardButton("Joined", callback_data="chatgpt")]])

@bot.on_message(filters.command("start") & filters.all)
async def start(bot, msg):
    reply_markup = START_BUTTON
    await msg.reply_text(text="<b>π§πΎπππ πΆπΎππΌπππΎ ππ π£ππππΎππ¦π―π³ π‘ππ. π³πππ π»ππ ππππππ½πΎ π’ππΊππ¦π―π³ & π³πΎππ ππ π¨ππΊππΎ π²πΎππππΌπΎπ.\n\nπ²πΎππΎπΌπ πΊ π²πΎππππΌπΎ πΏπππ π»πΎπππ π’ππππΊππ½π\n\nπ  π―πππ½ππΌπ ππΏ @TheDumperNetwork</b>", reply_markup=reply_markup)
    await bot.send_message(msg.chat.id, "<b>Use /ask For ChatGPT Questions</b>")

@bot.on_callback_query()
def callback_query(bot, CallBackQuery):
    reply_markup = START_BUTTON
    if CallBackQuery.data == "help":
        text = """
        <b>π’ππππΊππ½π π ππΊπππΊπ»ππΎ :\n/ask <q> - For chatGPT Questions\n\nπ€ππΊππππΎ :\n/ask what's 138 times 4</b>
        """
        CallBackQuery.edit_message_text(text, reply_markup=reply_markup)
    elif CallBackQuery.data == "source":
        text = "<b>π¨πΏ πππ ππΊππ ππππ π»ππ'π πππππΌπΎ πΌππ½πΎ\n\nπ’ππππΊπΌπ : @Walker_web</b>"
        CallBackQuery.edit_message_text(text, reply_markup=reply_markup)
    elif CallBackQuery.data == "back":
        text = "<b>π§πΎπππ πΆπΎππΌπππΎ ππ π£ππππΎππ¦π―π³ π‘ππ. π³πππ π»ππ ππππππ½πΎ π’ππΊππ¦π―π³ & π³πΎππ ππ π¨ππΊππΎ π²πΎππππΌπΎπ.\n\nπ²πΎππΎπΌπ πΊ π²πΎππππΌπΎ πΏπππ π»πΎπππ π’ππππΊππ½π\n\nπ  π―πππ½ππΌπ ππΏ @TheDumperNetwork</b>"
        CallBackQuery.edit_message_text(text, reply_markup=reply_markup)


@bot.on_message(filters.command("ask") & filters.all)
async def chatgpt(bot, msg):
    try:
        member = await bot.get_chat_member("DumperBots", msg.from_user.id)
        is_mem = True
    except UserNotParticipant:
        reply_markup = JOIN_BUTTON
        await msg.reply_text(text="<b>πΈππ ππππ ππππ πππ π’ππΊπππΎπ ππ πππΎ ππππ ππΎππππΌπΎ</b>", reply_markup=reply_markup)
        return

    if is_mem:
        prompt = msg.text.replace("/ask", "")
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
       
print("Bot is Running")
bot.run()
