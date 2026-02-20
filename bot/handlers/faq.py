from aiogram import Router, F
from aiogram.types import CallbackQuery

from bot.keyboards.inline import get_back_button
from bot.utils.texts import FAQ_TEXT

router = Router(name="faq")     # ← это обязательно должно быть!


@router.callback_query(F.data == "faq")
async def show_faq(callback: CallbackQuery):
    await callback.message.edit_text(
        FAQ_TEXT,
        reply_markup=get_back_button()
    )
    await callback.answer()