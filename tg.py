import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, CallbackQuery
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor


from platformas import djinni, remotebot,jobot,indeedbot


logging.basicConfig(level=logging.INFO)

bot_token = "6287333417:AAFQvVQCTdnU8aQDqUHX4U4lZZcpvdocyV0"

bot = Bot(token=bot_token)
dp = Dispatcher(bot)


# Başlangıç fonksiyonu
@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer("""
    Botdan istifadə etmək üçün aşağıdakı kommandlardan istifadə edə bilərsiniz:

/about Haqqımızda daha ətraflı məlumat əldə etmək istəyirsinizsə keçid edərsiniz.

/search Remote iş elanlarına baxmaq istəyirsinizsə, bura keçid edib baxa bilərsiniz.
    
    """)

# Başlangıç fonksiyonu
@dp.message_handler(commands=['about'])
async def start(message: Message):
    await message.answer("""
Alas Academy, fəaliyyətini 2020-ci ildə “TensorFlow User Group Azerbaijan” adı ilə başlamışdır və süni intellekt tədrisi ilə məşğul olmuşdur. 2022-ci ilin sonundan etibarən “Alas Academy” adi altında daha geniş sahələrin tədrisilə faəliyyətini davam etdirir.

Qafqazdakı Yeganə AWS partnyoru
Ölkədəki rəsmi TensorFlow User Group-u
100% ilə təmin olunma göstəricisi

Məqsədimiz Azərbaycan ərazisində IT icmasını inkişaf etdirməkdir.
    
    """)


# Başlangıç fonksiyonu
@dp.message_handler(commands=['search'])
async def search(message: Message):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("Front-end", callback_data='m1'),
        InlineKeyboardButton("Back-end", callback_data='m2'),
        InlineKeyboardButton("Data Science", callback_data='m3'),
        InlineKeyboardButton("Data analitc", callback_data='m4'),
        InlineKeyboardButton("Mobile Developer", callback_data='m5'),

    )
    await message.delete()
    await message.answer('Xoşgəldiniz! bir menu seçin:', reply_markup=keyboard)

# Menu 1 fonksiyonu
async def menu_1(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=3)
    keyboard.add(
        InlineKeyboardButton("React", callback_data='m1_1'),
        InlineKeyboardButton("Angular", callback_data='m1_2'),
        InlineKeyboardButton("Vuejs",callback_data="m1_3"),
        InlineKeyboardButton("Ana Menü", callback_data='main')
    )
    await callback_query.message.edit_text(text="Front-end, bir altmenü seçin:", reply_markup=keyboard)

# Menu 2 fonksiyonu
async def menu_2(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=3)
    keyboard.add(
        InlineKeyboardButton("Python", callback_data='m2_1'),
        InlineKeyboardButton("Java", callback_data='m2_2'),
        InlineKeyboardButton("Node.js",callback_data="m2_3"),
        InlineKeyboardButton("C#",callback_data="m2_4"),
        InlineKeyboardButton("PHP",callback_data="m2_5"),
        InlineKeyboardButton("Ana Menü", callback_data='main')
    )
    await callback_query.message.edit_text(text="Back-end, bir altmenü seçin:", reply_markup=keyboard)

async def menu_3(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=3)
    keyboard.add(
        InlineKeyboardButton("Android", callback_data='m3_1'),
        InlineKeyboardButton("IOS", callback_data='m3_2'),
        InlineKeyboardButton("Flutter",callback_data="m3_3"),
        InlineKeyboardButton("Ana Menü", callback_data='main')
    )
    await callback_query.message.edit_text(text="Back-end, bir altmenü seçin:", reply_markup=keyboard)

async def find_job(callback_query: CallbackQuery, job_type: str):
    send_message = ""
    for i in djinni.job_features(job_type):
        send_message = send_message + i + "\n\n"
    await bot.send_message(chat_id=callback_query.message.chat.id, text=send_message)

    send_message = ""
    for i in jobot.return_url(job_type):
        send_message = send_message + i + "\n\n"
    await bot.send_message(chat_id=callback_query.message.chat.id, text=send_message)

    send_message = ""
    for i in indeedbot.return_url(job_type):
        send_message = send_message + i + "\n\n"
    await bot.send_message(chat_id=callback_query.message.chat.id, text=send_message)

    send_message = ""
    for i in remotebot.return_url(job_type):
        send_message = send_message + i + "\n\n"
    await bot.send_message(chat_id=callback_query.message.chat.id, text=send_message)


# Callback query handler fonksiyonu
@dp.callback_query_handler()
async def button(callback_query: CallbackQuery):
    if callback_query.data == 'm1':
        await menu_1(callback_query)
    elif callback_query.data == 'm2':
        await menu_2(callback_query)
    elif callback_query.data == "m3":
        await find_job(callback_query,"data+science")
    elif callback_query.data == "m5":
        await menu_3(callback_query)
    elif callback_query.data == "m4":
        await find_job(callback_query,"data+analitic")
    elif callback_query.data == 'm1_1':
        await find_job(callback_query, "React")
    elif callback_query.data == 'm1_2':
        await find_job(callback_query, "Angular")
    elif callback_query.data == 'm1_3':
        await find_job(callback_query, "Vuejs")
    elif callback_query.data == 'm2_1':
        await find_job(callback_query, "Python")
    elif callback_query.data == 'm2_2':
        await find_job(callback_query, "Java")
    elif callback_query.data == 'm2_3':
        await find_job(callback_query, "Node.js")
    elif callback_query.data == 'm2_4':
        await find_job(callback_query, "C#")
    elif callback_query.data == 'm2_5':
        await find_job(callback_query, "laravel")
    elif callback_query.data == 'm3_1':
        await find_job(callback_query, "android")
    elif callback_query.data == 'm3_2':
        await find_job(callback_query, "ios")
    elif callback_query.data == 'm3_3':
        await find_job(callback_query, "flutter")

    elif callback_query.data == 'main':
        await search(callback_query.message)

if __name__ == '__main__':
    executor.start_polling(dp)
