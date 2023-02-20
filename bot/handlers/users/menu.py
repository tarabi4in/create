from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor


@dp.message_handler(content_types=['text'])
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'Damn':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Инструкция 1')
            item2 = types.KeyboardButton('Старт')
            markup.add(item1, item2)

            await message.answer('Damn', reply_markup=markup)


