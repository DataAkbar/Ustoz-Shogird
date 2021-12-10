from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from keyboards.default.new import menu


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    kirish = "UstozShogird kanalining rasmiy botiga xush kelibsiz!,\
        \n/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!"
    await message.answer(f"Assalomu-alaykum, {message.from_user.full_name}!\n\n{kirish} ", reply_markup=menu)
