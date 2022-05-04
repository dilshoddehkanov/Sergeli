from aiogram.dispatcher.filters.state import StatesGroup, State


class sergeli(StatesGroup):
    name = State()
    surname = State()
    phone = State()
    age = State()
