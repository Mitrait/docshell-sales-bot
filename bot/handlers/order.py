from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from bot.states.order import OrderForm
from bot.keyboards.inline import get_back_button, get_confirm_keyboard, get_main_menu
from bot.utils.texts import ORDER_START
from config.config import ADMIN_ID, SUPPORT_NAME, SUPPORT_PHONE, SUPPORT_EMAIL

router = Router(name="order")


@router.callback_query(F.data == "order_start")
async def order_start(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text(ORDER_START, reply_markup=get_back_button())
    await state.set_state(OrderForm.name)
    await callback.answer()


@router.message(OrderForm.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text.strip())
    await message.answer("Название компании / организации / ИП:")
    await state.set_state(OrderForm.company)


@router.message(OrderForm.company)
async def process_company(message: Message, state: FSMContext):
    await state.update_data(company=message.text.strip())
    await message.answer("ИНН компании (10 или 12 цифр):")
    await state.set_state(OrderForm.inn)


@router.message(OrderForm.inn)
async def process_inn(message: Message, state: FSMContext):
    await state.update_data(inn=message.text.strip())
    await message.answer("Ваш контактный телефон:")
    await state.set_state(OrderForm.phone)


@router.message(OrderForm.phone)
async def process_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text.strip())
    await message.answer("Ваш email для связи:")
    await state.set_state(OrderForm.email)


@router.message(OrderForm.email)
async def process_email(message: Message, state: FSMContext):
    await state.update_data(email=message.text.strip())
    await message.answer("Дополнительный комментарий / пожелания (можно пропустить):")
    await state.set_state(OrderForm.comment)


@router.message(OrderForm.comment)
async def process_comment_and_confirm(message: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    comment = message.text.strip() if message.text else "—"

    summary = f"""<b>НОВАЯ ЗАЯВКА на DocShell</b>

Имя:          {data.get('name', '—')}
Компания:     {data.get('company', '—')}
Телефон:      {data.get('phone', '—')}
Комментарий:  {comment}

От: @{message.from_user.username or message.from_user.id}"""

    if ADMIN_ID:
        try:
            await bot.send_message(ADMIN_ID, summary)
        except:
            pass  # если админ заблокировал бота — просто продолжаем

    await message.answer(
        f"Заявка успешно отправлена!\n\n{SUPPORT_NAME} свяжется с вами в ближайшее время.\n\n"
        f"📞 {SUPPORT_PHONE}\n"
        f"📧 {SUPPORT_EMAIL}",
        reply_markup=get_main_menu()
    )

    await state.clear()