from aiogram import Router, types
from aiogram.filters import Command
import os
import aiohttp

router = Router()
ADMIN_CHAT_ID = 382094545

API_URL = os.getenv("API_URL", "http://backend:8000")

@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Добро пожаловать! Для бронирования пользуйтесь сайтом.")

@router.message(Command("add_car"))
async def add_car(message: types.Message):
    if message.from_user.id != ADMIN_CHAT_ID:
        return await message.answer("Нет доступа")
    car_name = message.text.split(maxsplit=1)[-1]
    async with aiohttp.ClientSession() as session:
        await session.post(f"{API_URL}/car/", json={"name": car_name})
    await message.answer(f"Автомобиль {car_name} добавлен.")

@router.message(Command("delete_car"))
async def delete_car(message: types.Message):
    if message.from_user.id != ADMIN_CHAT_ID:
        return await message.answer("Нет доступа")
    car_id = message.text.split(maxsplit=1)[-1]
    async with aiohttp.ClientSession() as session:
        await session.delete(f"{API_URL}/car/{car_id}")
    await message.answer(f"Автомобиль ID {car_id} удалён.")
