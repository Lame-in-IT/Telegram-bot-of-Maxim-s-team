from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButtonRequestUser

# --- Main Menu ---
request_button = KeyboardButton(text="Добавить контакты для рассылки", request_user=KeyboardButtonRequestUser(request_id=1))
btnapi = KeyboardButton('Удалить контакты для рассылки', resize_keyboard=True) # type: ignore
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(request_button).add(btnapi) # type: ignore

def del_contac(data): # передаём в функцию data
    genmarkup = InlineKeyboardMarkup() # создаём клавиатуру
    genmarkup.add(InlineKeyboardButton(text="Удалить", callback_data=data)) # type: ignore #Создаём кнопки, data - название, data - каллбек дата
    return genmarkup #возвращаем клавиатуру