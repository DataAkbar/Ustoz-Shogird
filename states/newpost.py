from os import name
from aiogram.dispatcher.filters.state import StatesGroup, State

class NewPost(StatesGroup):
    name = State()
    old = State()
    tech = State()
    phone = State()
    address = State()
    price = State()
    job = State()
    time = State()
    maqsad = State()
    # image = State()
    confirm = State()