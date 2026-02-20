import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties          # ← добавили
from aiogram.enums import ParseMode                              # ← добавили

from config.config import BOT_TOKEN
from bot.handlers import start, menu, demo, order, faq, support

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)   # ← правильный способ
    )
    dp = Dispatcher(storage=MemoryStorage())

    # Подключаем все роутеры
    dp.include_routers(
        start.router,
        menu.router,
        demo.router,
        order.router,
        faq.router,
        support.router
    )

    print("🚀 DocShell Sales Bot 2026 запущен!")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())