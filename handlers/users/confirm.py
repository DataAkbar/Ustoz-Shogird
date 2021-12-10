from aiogram.types.user import User
from loader import dp, bot
from aiogram.types import CallbackQuery, message
from aiogram import types
from aiogram.dispatcher import FSMContext
from data.config import ADMINS, CHANNELS
from keyboards.default.new import menu
from keyboards.inline.admin import confirmation_keyboard
from states.newpost import NewPost
from loader import dp, bot

@dp.callback_query_handler(text='confirm', state=NewPost.confirm)
async def confirm_post(call: CallbackQuery, state: FSMContext):
    # Ma'lumotlarni qayta o'qiymiz
    data = await state.get_data()
    name = data.get('name')
    old = data.get('old')
    tech = data.get('tech')
    # name = data.get('name')
    phone = data.get('phone')
    address = data.get('address')
    price = data.get('price')
    job = data.get('job')
    time = data.get('time')
    maqsad = data.get('maqsad')
    # image = data.get('image')

    # name = bot.get(User.full_name)
    msg = f"❗️❗️❗️ <b>Ustoz kerak:</b>\n\n"
    msg += f"🎓 Shogird:  {name}\n"
    msg += f"🌐 Yosh:  {old}\n"
    msg += f"📚 Texnologiya:{tech}\n"
    msg += f"🇺🇿 Telegram:{None}\n"
    msg += f"📞 Aloqa: {phone}\n"
    msg += f"🌐 Hudud: {address}\n"
    msg += f"💰 Narxi:  {price}\n"
    msg += f"👨🏻‍💻 Kasbi: {job}\n"
    msg += f"🕰 Murojaat qilish vaqti: {time}\n"
    msg += f"🔎 Maqsad: {maqsad}\n"
    for i in ADMINS:
        await bot.send_message(i, msg, reply_markup=confirmation_keyboard)
    await call.message.edit_reply_markup()
    await state.finish()


@dp.callback_query_handler(text='cancel', state=NewPost.confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("Bekor qilindi", reply_markup=menu)
    await state.finish()


@dp.callback_query_handler(text='admin_confirm')
async def confirm_post(call: CallbackQuery):
    message = await call.message.edit_reply_markup()
    await message.send_copy(chat_id=CHANNELS[0])


@dp.callback_query_handler(text='admin_cancel')
async def cancel_post(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Bekor qilindi")
