import asyncio
from aiogram import Bot, Dispatcher
from handlers import router
import os

BOT_TOKEN = os.getenv("6602514727:AAF7d2iEQmH5YbynKSZH-lPA9-BDUNmjphY")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
