import logging
from aiogram import Bot, Dispatcher, executor, types
from CheckWord import checkWord


API_TOKEN = '6125175508:AAFtjcSJtah3UXRWvffXr9IWHrBneTybXXc'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.reply("Salom\nMening ikkinchi imlo botimga xush kelibsiz !!!\n")

@dp.message_handler(commands='rasm')
async def rasm(message: types.Message):
    await message.answer_photo('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTblImrbtf3iDl_ttgkGETWD57OXZM15DV_iw&usqp=CAU')

@dp.message_handler(commands='help')
async def help_user(message: types.Message):
    await message.reply("botdan foydalanish uchun biror so'z yuboring :")

@dp.message_handler()
async def checkImlo(message: types.Message):
    word = message.text
    result = checkWord(word)
    if result['available']:
        response = f"✅ {word.capitalize()}\n"
    else:
        response = f"❌ {word.capitalize()}\n"
        for text in result['matches']:
            response += f"✅ {text.capitalize()}\n"
    await message.answer(response)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)