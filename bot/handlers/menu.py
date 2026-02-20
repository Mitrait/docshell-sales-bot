from aiogram import Router, F
from aiogram.types import CallbackQuery

from bot.keyboards.inline import get_main_menu, get_back_button
from bot.utils.texts import INFO_TEXT, PRICES_TEXT, FAQ_TEXT, WELCOME

router = Router(name="menu")


@router.callback_query(F.data == "main_menu")
async def back_to_main(callback: CallbackQuery):
    await callback.message.edit_text(WELCOME, reply_markup=get_main_menu())
    await callback.answer()


@router.callback_query(F.data == "info")
async def show_info(callback: CallbackQuery):
    await callback.message.edit_text(INFO_TEXT, reply_markup=get_back_button())
    await callback.answer()


@router.callback_query(F.data == "prices")
async def show_prices(callback: CallbackQuery):
    await callback.message.edit_text(PRICES_TEXT, reply_markup=get_back_button())
    await callback.answer()


@router.callback_query(F.data == "faq")
async def show_faq(callback: CallbackQuery):
    await callback.message.edit_text(FAQ_TEXT, reply_markup=get_back_button())
    await callback.answer()