from aiogram import Bot, Dispatcher, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup

API_TOKEN = '6196927890:AAFzR2L4hr8WuO7ZhTyT390vItif9ylGFM8'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

iphones = {
    'iphone 12': 50000,
    'iphone 11': 40000,
    'iphone 13': 60000,
    'iphone 14': 70000,
    'iphone 12 Pro': 60000,
    'iphone 13 Pro': 70000,
    'iphone 11 Pro': 90000,
}
# Клавиатуры
# Главная клавиатура
kb_btns = [
    [KeyboardButton(text='Цена'), KeyboardButton(text='О нас')],
]
kb_main = ReplyKeyboardMarkup(keyboard=kb_btns, resize_keyboard=True)
kb_buttons = []
for key in iphones:
    button = [KeyboardButton(text=key, callback_data=key)]
    kb_buttons.append(button)
kb_models = InlineKeyboardMarkup(inline_keyboard=kb_buttons)

# Хендлеры
async def start_handler(message):
    await message.answer('Привет! Я бот, умею ...', reply_markup=kb_main) 

async def about_handler(message):
    await message.answer('Мы - компания, которая любит пайкьюти')

async def price_handler(message):
    await message.answer('В наличии есть такие айфоны:', reply_markup=kb_models)

async def show_price_handler(callback):
    await callback.message.answer(iphones[callback.data])

# Регистрация хендлеров
dp.register_message_handler(start_handler, commands=['start'])
dp.register_message_handler(about_handler, lambda mes: mes.text == 'О нас')
dp.register_message_handler(price_handler, lambda mes: mes.text == 'Цена')
dp.register_callback_query_handler(show_price_handler, lambda cb: cb.data.startswith('iphone'))
# Запуск бота
executor.start_polling(dp, skip_updates=True)















