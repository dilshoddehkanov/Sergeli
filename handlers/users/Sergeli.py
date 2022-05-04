import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from loader import dp, bot
from states.Sergeli import sergeli
from keyboards.default.Keyboards import location


@dp.message_handler(text='Suzish havzasi uchun ro\'yxatdan o\'tish.')
async def take_suzish(message: Message, state: FSMContext):
    await message.answer('Ismingizni kiriting', reply_markup=ReplyKeyboardRemove())
    await sergeli.name.set()


@dp.message_handler(state=sergeli.name)
async def take_name(message: Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {'name': name}
    )
    await message.answer('Familiyangizni kiriting')
    await sergeli.surname.set()


@dp.message_handler(state=sergeli.surname)
async def take_surname(message: Message, state: FSMContext):
    surname = message.text
    await state.update_data(
        {'surname': surname}
    )
    await message.answer('Telefon raqamingizni +998901234567 ko\'rinishda kiriting')
    await sergeli.phone.set()


@dp.message_handler(state=sergeli.phone)
async def take_phone(message: Message, state: FSMContext):
    phone = message.text
    await state.update_data(
        {'phone': phone}
    )
    await message.answer('Yoshingnizni kiriting:')
    await sergeli.age.set()


@dp.message_handler(state=sergeli.age)
async def take_age(message: Message, state: FSMContext):
    data = await state.get_data()
    name = data.get('name')
    surname = data.get('surname')
    username = (await dp.bot.get_me()).username
    phone = data.get('phone')
    try:
        age = int(message.text)
        if (age >= 7) and (age <= 11):
            await message.answer_photo('https://t.me/foto_va_mp3lar_olami_575/123',
                                       caption=f"Sizni ro'yhatga oldik, namunadagi hujjatlarni 7 ish kun oralig'ida "
                                               f"olib kelishingizni so'raymiz\n\n\n"
                                               f"🔥 @{username.capitalize()}", reply_markup=location)
            target_channel = '-1001738599887'
            await bot.send_message(chat_id=target_channel, text=f'Ism:    {name},\n'
                                                                f'Familiya:    {surname},\n'
                                                                f'Telefon raqam:    {phone}\n'
                                                                f'Yosh:    {age}\n\n'
                                                                f'🔥 @{username.capitalize()}')
        else:
            await message.answer('Kechirasiz, bizning suzish havzamiz faqatgina 7-11 yosh oralig\'idagilar uchun.',
                                 reply_markup=location)
        await state.finish()
    except:
        await message.answer('Yoshingizni faqat son ko\'rinishida (Masalan, 21) jo\'nating')
        await sergeli.age.set()


@dp.message_handler(text='Manzil')
async def send_location(message: Message):
    await bot.send_location(chat_id=message.from_user.id, latitude='41.224499', longitude='69.212434')
