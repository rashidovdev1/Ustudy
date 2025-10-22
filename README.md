# BOT KODI QANDAY ISHLAYDI

### Importlar:
```python
from aiogram import Bot, Dispatcher, types
"""aiogram kutubxonasidan Bot (Telegram botini boshqaradi), 
Dispatcher (xabarlarni boshqaradi) va 
types (turli Telegram obyektlari)ni import qilamza"""

from aiogram.types import Message
"""Message — foydalanuvchidan kelgan xabarla u-n klass. 
Bu yordamida message.text, message.from_user, va h.k. ishlatamz"""

from aiogram.enums import ParseMode
"""ParseMode.HTML yoki Markdown formatda xabar yuborish un kk. 
Masalan <b>qalin</b> yoki *bold*"""

from aiogram.filters import CommandStart
"""Bu filter /start komandasi yuborilganda ishlaydigan handlerni aniqlaydi"""

from aiogram.client.default import DefaultBotProperties
"""Bu yordamida parse_mode kabi sozlamalani Bot ichida default sifatida o‘rnatamz"""

import asyncio
"""aiogram asinxron kutubxona bo‘lgani uchun asyncio kerak
Bu yordamida async funksiyalarni bajarish mkn"""

TOKEN = "TOKEN yozing"
""" BotFatherdan olingan TOKEN shotga yoziladi,token botga kirish kaliti"""

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
"""Bot obyektini yaratdik. Bu obyekt orqali siz botga xabar yuborasz
default=... — bu bot har doim HTML formatda xabar yuborishini bildiradi"""

dp = Dispatcher()
"""Dispatcher obyektini yaratamza — 
bu botga kelayotgan xabarla ii komandalani handlerlarga yo‘naltiradi"""

@dp.message(CommandStart())
async def start_handler(message: Message):
   await message.answer("Salom! Men Echo botman. Nima yozsangiz, o‘shani qaytaraman")
"""Foydalanuvchi /start deb yozsa, shu funksiya ishga tushadi.
message.answer() — bu foydalanuvchiga javob yozadi"""

@dp.message()
async def echo_handler(message: Message):
    await message.answer(message.text)
"""Bu echo handler — foydalanuvchi nima yozsa, bot aynan o‘sha matnni qaytaradi"""

async def main():
    await dp.start_polling(bot)
"""Bu main() funksiyasi botni polling rejimida ishga tushiradi 
ya'ni doimiy ravishda Telegram serveridan xabarlarni tekshiradi"""

if __name__ == "__main__":
    asyncio.run(main())
"""Python fayl togridan-togri ishga tushirilganda main() funksiyasini bajar degani"""
