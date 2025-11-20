from aiogram import Bot, Dispatcher, types, F
from aiogram.types import WebAppInfo
import config

bot = Bot(config.BOT_TOKEN)
dp = Dispatcher()


@dp.message(F.text == "/start")
async def start(message: types.Message):

    photo = types.FSInputFile(config.WELCOME_IMAGE)
    await message.answer_photo(photo, caption=config.WELCOME_TEXT)

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(
                    text="Открыть приложение",
                    web_app=WebAppInfo(url=config.MINI_APP_URL)
                )
            ]
        ],
        resize_keyboard=True
    )

    await message.answer("Нажмите кнопку ниже 👇", reply_markup=keyboard)
