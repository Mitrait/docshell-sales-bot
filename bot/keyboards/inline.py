from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_main_menu():
    kb = [
        [InlineKeyboardButton(text="🔥 Что такое DocShell?", callback_data="info")],
        [InlineKeyboardButton(text="🎁 Бесплатная демо-версия", callback_data="demo")],
        [InlineKeyboardButton(text="💰 Тарифы 2026", callback_data="prices")],
        [InlineKeyboardButton(text="🛡️ Заказать внедрение", callback_data="order_start")],
        [InlineKeyboardButton(text="❓ Частые вопросы (FAQ)", callback_data="faq")],
        [InlineKeyboardButton(text="👨‍💼 Связь с представителем в Сочи", callback_data="support")],
        [InlineKeyboardButton(text="🌐 Официальный сайт", url="https://docshell.ru")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)


def get_back_button():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="← Вернуться в меню", callback_data="main_menu")]
    ])


def get_confirm_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Всё верно, отправить", callback_data="confirm")],
        [InlineKeyboardButton(text="← Исправить", callback_data="order_start")],
    ])