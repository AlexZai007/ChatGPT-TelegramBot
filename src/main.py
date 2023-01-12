from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import Config
from termcolor import cprint

import asyncio


bot = Bot(token = Config.telegram_token)
dp = Dispatcher(bot = bot, storage=MemoryStorage())


async def main():

    print('➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
    cprint('🔱 Бот был написан гением - AlexZai007', "cyan")
    print('➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')

    from handlers import dp

    try:
        print('➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
        cprint("✅ Успешно - Бот установил связь с сервером телеграм ", "green")
        print('➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
        await dp.start_polling()
    finally:
        cprint("❌Остоновлен - бот остановил связь с сервером", "red")


if __name__ == "__main__":
    try:
        # run the main function
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        cprint("❌Остоновлен - Бот остоновлен пользователем", "red")
