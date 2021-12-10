from aiogram.types.user import User
from loader import dp, bot
from aiogram import types
from states.newpost import NewPost
from aiogram.dispatcher import FSMContext
from keyboards.inline.manage import confirmation_keyboard

@dp.message_handler(text_contains="Ustoz kerak", state=None)
async def new_posts(message: types.Message):
    chuntirish = "Hozir sizga birnecha savollar beriladi.\n\
Har biriga javob bering.\n\
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va \
arizangiz Adminga yuboriladi."
    await message.answer(f"Ustoz topish uchun ariza berish\n\n{chuntirish}")
    await message.answer(f"Ism, familiyangizni kiriting?")
    await NewPost.name.set()

@dp.message_handler(state=NewPost.name)
async def name(message: types.Message, state: FSMContext):
    name = message.text

    await state.update_data(
        {'name': name}
    )
    await message.answer("🕔 Yosh:\n\nYoshingizni kiriting\nMasalan: 19")
    await NewPost.old.set()


@dp.message_handler(state=NewPost.old)
async def olds(message: types.Message, state: FSMContext):
    old = message.text

    await state.update_data(
        {'old': old}
    )
    await message.answer("📚 Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting!\nTexnologiya nomlarini vergul bilan ajrating.Masalan:\n\nPython,C++,C#")
    await NewPost.tech.set()


@dp.message_handler(state=NewPost.tech)
async def techh(message: types.Message, state: FSMContext):
    tech = message.text

    await state.update_data(
        {'tech': tech}
    )
    await message.answer("📞 Aloqa:\n\nBog`lanish uchun raqamingizni kiriting!\nMasalan, +998 90 123 45 67")
    await NewPost.phone.set()


@dp.message_handler(state=NewPost.phone)
async def phonne(message: types.Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {'phone': phone}
    )
    await message.answer("🌐 Hudud:\n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.")
    await NewPost.address.set()


@dp.message_handler(state=NewPost.address)
async def addressw(message: types.Message, state: FSMContext):
    address = message.text

    await state.update_data(
        {'address': address}
    )
    await message.answer("💰 Narxi:\n\nTolov qilasizmi yoki Tekinmi?\nKerak bo`lsa, Summani kiriting?")
    await NewPost.price.set()


@dp.message_handler(state=NewPost.price)
async def pricce(message: types.Message, state: FSMContext):
    price = message.text

    await state.update_data(
        {'price': price}
    )
    await message.answer("👨🏻‍💻 Kasbi:\n\nIshlaysizmi yoki o`qiysizmi?\nMasalan, Talaba")
    await NewPost.job.set()


@dp.message_handler(state=NewPost.job)
async def job(message: types.Message, state: FSMContext):
    job = message.text

    await state.update_data(
        {'job': job}
    )
    await message.answer("🕰 Murojaat qilish vaqti:\n\nQaysi vaqtda murojaat qilish mumkin?\nMasalan, 9:00 - 18:00")
    await NewPost.time.set()


@dp.message_handler(state=NewPost.time)
async def time(message: types.Message, state: FSMContext):
    time = message.text

    await state.update_data(
        {'time': time}
    )
    await message.answer("🔎 Maqsad:\n\nMaqsadingizni qisqacha yozib bering.")
    await NewPost.maqsad.set()


@dp.message_handler(state=NewPost.maqsad)
async def maqsad(message: types.Message, state: FSMContext):
    maqsad = message.text

    await state.update_data(
        {'maqsad': maqsad}
    )

    # Ma'lumotlarni qayta o'qiymiz
    data = await state.get_data()
    name = data.get('name')
    old = data.get('old')
    tech = data.get('tech')
    phone = data.get('phone')
    address = data.get('address')
    price = data.get('price')
    job = data.get('job')
    time = data.get('time')
    maqsad = data.get('maqsad')
    # price = data.get('price')
    # image = data.get('image')

    # name = bot.get(User.username)
    msg =  f"📄 <b>Ustoz kerak:</b>\n\n"
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
    await message.answer(msg, reply_markup=confirmation_keyboard)
    await NewPost.next()
    # await state.finish()