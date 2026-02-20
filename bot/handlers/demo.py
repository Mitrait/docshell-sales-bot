from aiogram import Router, F
from aiogram.types import CallbackQuery

from bot.keyboards.inline import get_back_button

router = Router(name="demo")


@router.callback_query(F.data == "demo")
async def show_demo(callback: CallbackQuery):
    text = """<b>Бесплатная демонстрация DocShell</b> 🎥

Мы предоставим тестовый доступ на 7–14 дней + персональную демонстрацию.

Чтобы получить демо:
1. Оставьте заявку (кнопка «Заказать внедрение»)
2. Или напишите напрямую представителю в Сочи

Ждём ваших данных! 👇"""

    await callback.message.edit_text(text, reply_markup=get_back_button())
    await callback.answer()