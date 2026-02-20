from aiogram import Router, F
from aiogram.types import CallbackQuery

from bot.keyboards.inline import get_back_button
from bot.utils.texts import SUPPORT_TEXT

router = Router(name="support")


@router.callback_query(F.data == "support")
async def show_support(callback: CallbackQuery):
    await callback.message.edit_text(SUPPORT_TEXT, reply_markup=get_back_button())
    await callback.answer()