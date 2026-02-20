from aiogram.fsm.state import State, StatesGroup


class OrderForm(StatesGroup):
    name = State()
    company = State()
    inn = State()
    phone = State()
    email = State()
    comment = State()