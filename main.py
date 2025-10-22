"""ECHO BOT |04.05.2025"""

from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties
import asyncio

# TOKENga @botfather bergan API yozing
TOKEN = "TOKEN"

# parse_mode endi 'default' parametri orqali beriladi
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Salom! Men Echo botman.Nima yozsangiz o‘shani qaytaraman🙂")

@dp.message()
async def echo_handler(message: Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())