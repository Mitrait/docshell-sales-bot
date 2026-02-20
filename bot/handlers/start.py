from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.keyboards.inline import get_main_menu
from bot.utils.texts import WELCOME

router = Router(name="start")


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        WELCOME,
        reply_markup=get_main_menu(),
        disable_web_page_preview=True
    )