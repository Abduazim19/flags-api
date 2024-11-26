from aiogram import Dispatcher, Bot, types, executor
import requests

token = '7263286065:AAGjDaY6ju0hqNU-guwMkW-SFpHko1zVvd0'
bot = Bot(token=token)
dp = Dispatcher(bot)

flags = requests.get('https://flags-api-pn1k.onrender.com/api/').json()

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Hello, I'm a simple bot. Type /help for more information.")



@dp.message_handler()
async def echo(message: types.Message):
    davlat = message.text
    bayroq_url = ""
    for flag in flags:
        if davlat == flag["country_name"]:
            bayroq_url = flag["images"]
            bayroq_url = bayroq_url[21:]
            print(bayroq_url)

    try:
        bayroq = types.InputFile(f"..{bayroq_url}")
        await message.answer_photo(photo=bayroq_url, caption=davlat)
    except Exception as e:
        await message.reply(f"Rasimni yuborishda xatolik yuz berdi {e}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)