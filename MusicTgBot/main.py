import asyncio
import logging
import os
import sys
import time

from function import downloadingMusic, downloadPlaylist

from config import TOKEN_API, HELP1, HELLO_TEXT
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import FSInputFile
from aiogram.types import URLInputFile
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


HELP_COMMAND = HELP1

TOKEN = TOKEN_API
dp = Dispatcher()
bot1 = Bot(TOKEN)


@dp.message(Command("help"))
async def help_message(message: types.Message):
    await message.reply(text=HELP_COMMAND, parse_mode='HTML')


@dp.message(Command("start"))
async def start_message(message: types.Message):
    await message.answer(HELLO_TEXT)
    await message.delete()


@dp.message(Command("sticker"))
async def start_message(message: types.Message):
    await asyncio.sleep(5)
    await bot1.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAI8gGTzdbLbKytgM8vuykBJVXNcT4s9AAJpAQACEBptItP50YqvnDOtMAQ')


#@dp.message()
async def playlist_download(message: types.Message) -> None:
    playlist_link = message.text
    playlist_link = playlist_link[10:]
    playlist_photo = ""
    result = downloadPlaylist(playlist_link, playlist_photo)
    link1 = result[0]
    photo1 = result[1]
    print(result)
    print(link1)
    print(photo1)
    link1 = link1.split(", ")
    i = 1
    while i <= (len(link1)+1):
        time.sleep(2)
        print(i)
        name = link1[i]
        print(name)
        #photo = photo1[i]
        #print(photo)
        path = f'C:/Users/Dimas/Downloads/{name}'
        audio = FSInputFile(path)
        name = name[:-4]
        name = f"{name}.jpg"
        #photo = URLInputFile(photo, filename=name)
        #await bot1.send_photo(message.from_user.id, photo)
        await bot1.send_audio(message.from_user.id, audio)
        os.remove(path)
        i += 1


@dp.message()
async def music(message: types.Message) -> None:
        word = "track"
        a = message.text
        if word in a:
            print(a)
            result1 = downloadingMusic(message.text, a)
            result = result1[0]
            a = result1[1]
            path = f'C:/Users/Dimas/Downloads/{result}'
            audio = FSInputFile(path)
            result = result[:-4]
            result = f'{result}.jpg'
            a = URLInputFile(a, filename=result)
            await bot1.send_photo(message.from_user.id, a)
            await bot1.send_audio(message.from_user.id, audio)
            os.remove(path)
            await message.delete()
        else:
            await message.answer("Работает только с сылками")




@dp.message()
async def echo_handler(message: types.Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


@dp.message()
async def echo(message: Message) -> None:
    print(f'{message.from_user.username} отправил: {message.text}')


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
