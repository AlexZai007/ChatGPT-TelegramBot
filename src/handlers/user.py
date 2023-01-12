import aiogram
from aiogram.types import LabeledPrice, Message, PreCheckoutQuery, ContentType, ShippingQuery, ShippingOption
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Command
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import BotBlocked
from aiogram.types import CallbackQuery
import asyncio


from src.main import bot, dp
from src.config import Config
from src.service.animation import generate_generation_message
from src.service import GPT
Chat = GPT(Config.open_ai_token)


print("✅ Успешно - geter ")


@dp.message_handler(commands="start")
async def start(message: Message):
    await bot.send_message(message.chat.id, """
🤿Что бы <b>начать</b> работу просто введите любой запрос на (русском/английском) языке.
    
❤Для лучшей работы пишите запросы исключительно на <b>английском</b> языке.

🔥<b>Автор</b>: Господин Александр    
""", parse_mode="HTML")


@dp.message_handler()
async def main(message: Message):


    my_new_message = await generate_generation_message(message, 10)
    try:
        response = await Chat.SendText(message.text)

        await bot.edit_message_text(chat_id=message.chat.id, message_id=my_new_message.message_id, text=f"""
📤 <b> Запрос </b>

{message.text}


📩 <b> Ответ </b>
{response['choices'][0]['text']}
""", parse_mode="HTML")
    except Exception:
        await bot.edit_message_text(chat_id=message.chat.id, message_id=my_new_message.message_id, text=f"🛑Случилась фатальная ошибка (обратитесь к господину)")
