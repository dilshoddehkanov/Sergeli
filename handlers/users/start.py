from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from states.Sergeli import sergeli
from keyboards.default.Keyboards import Main_Menu


@dp.message_handler(CommandStart(), state='*')
@dp.message_handler(text='Asosiy menu')
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=Main_Menu)
    await state.finish()
