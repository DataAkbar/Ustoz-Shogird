from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import CallbackQuery
from loader import dp

@dp.callback_query_handler(text='damas')
async def damas(call: CallbackQuery):
    await call.message.answer("Damas haqida")