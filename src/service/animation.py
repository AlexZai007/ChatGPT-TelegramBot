import aiogram
import asyncio
import random
from aiogram.dispatcher import FSMContext
from aiogram.types import LabeledPrice, Message, PreCheckoutQuery, ContentType, ShippingQuery, ShippingOption
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Command
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import BotBlocked

from src.main import bot

'''
🧠 function to animate the loading request.

📝 Change the text yourself. The maximum delay of 1 second to change 1 message (if time = 10) count on this.

🔥 An effective animation was made in order to stop a large flow of information and so that the API would not be banned. 
This will not save you from spam, but it will help you process much fewer requests and improve the user experience.

'''

#animation
async def generate_generation_message(message, time):

    my_new_message = await bot.send_message(message.chat.id, '🎯 Входные даные полученны!')
    await asyncio.sleep(3)
    await bot.edit_message_text(chat_id=message.chat.id, message_id=my_new_message.message_id, text='🎯 Сервер принял даные')
    await asyncio.sleep(random.randint(1, 10)/time)
    await bot.edit_message_text(chat_id=message.chat.id, message_id=my_new_message.message_id, text='⭐ Сервер обработал 1/5 фрагментов')
    await asyncio.sleep(random.randint(1, 10)/time)
    await bot.edit_message_text(chat_id=message.chat.id, message_id=my_new_message.message_id, text='⭐ Сервер обработал 2/5 фрагментов')
    await asyncio.sleep(random.randint(1, 10)/time)
    await bot.edit_message_text(chat_id=message.chat.id, message_id=my_new_message.message_id, text='⭐ Сервер обработал 3/5 фрагментов')
    await asyncio.sleep(random.randint(1, 10)/time)
    await bot.edit_message_text(chat_id=message.chat.id, message_id=my_new_message.message_id, text='⭐ Сервер обработал 4/5 фрагментов')
    await asyncio.sleep(random.randint(1, 10)/time)
    await bot.edit_message_text(chat_id=message.chat.id, message_id=my_new_message.message_id, text='⭐ Сервер обработал 5/5 фрагментов')
    await asyncio.sleep(random.randint(1, 10)/time)
    await bot.edit_message_text(chat_id=message.chat.id, message_id=my_new_message.message_id, text='✅ Успешно!')
    await asyncio.sleep(random.randint(1, 10) / time)
    await bot.edit_message_text(chat_id=message.chat.id, message_id=my_new_message.message_id, text='💎 Генерируем ответ...')
    await asyncio.sleep(random.randint(1, 10) / time)

    return my_new_message