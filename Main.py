import time
from token_bot import TOKIN
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
from aiofiles import os

from connect_bd import *
from markups import *

bot = Bot(token=TOKIN, parse_mode="HTML")
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def command_start(message: types.Message):
    if message.chat.type == 'private':
        hello_user = read_user(message["from"])
        await bot.send_message(message.from_user.id, f'{hello_user} {message["from"]["first_name"]}'.format(message.from_user), reply_markup=nav.mainMenu)


@dp.message_handler(commands=["help"])
async def command_help(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, f'{message["from"]["first_name"]} вам нужна помощь?'.format(message.from_user), reply_markup=nav.mainMenu)
        
@dp.message_handler(content_types=types.ContentType.USER_SHARED)
async def on_user_shared(message: types.Message):
    if message.from_user.id == 1323522063:
        req_cont = create_comtact(message.from_user.id, message.user_shared.user_id)
        await bot.send_message(message.from_user.id, f"{req_cont}.".format(message.from_user), reply_markup=nav.mainMenu)
    else:
        await bot.send_message(message.from_user.id, "У вас нет прав добавлять контакты.".format(message.from_user), reply_markup=nav.mainMenu)
    
@dp.message_handler(text="Удалить контакты для рассылки")
async def del_contact(message: types.Message):
    if message.from_user.id == 1323522063:
        data_cont = get_contact(message.from_user.id)
        for index, item in enumerate(data_cont[0]):
            await bot.send_message(message.from_user.id, f"Имя - {item}\n"
                                   f"Ник в телеграмм - {data_cont[1][index]}\n".format(message.from_user), reply_markup=del_contac(data_cont[2][index]))
    else:
        await bot.send_message(message.from_user.id, "У вас нет контактов.".format(message.from_user), reply_markup=nav.mainMenu)
        
@dp.callback_query_handler()
async def callback_1(callback: types.CallbackQuery):
    id_user = callback["message"]["chat"]["id"]
    contact = callback["message"]["reply_markup"]["inline_keyboard"][0][0]["callback_data"]
    req = delet_cont(id_user, contact)
    await bot.send_message(callback.from_user.id, f"{req}".format(callback.from_user), reply_markup=nav.mainMenu)
    
    
@dp.message_handler(text="diff")
async def get_no_sales_wb(message: types.Message):
    get_satat = get_sales_today()
    for item_id_user in get_satat[5]:
        try:
            for index, satat in enumerate(get_satat[4]):
                await bot.send_message(item_id_user,
                                    f'Артикул -   {get_satat[0][index]} шт.\n'
                                    f'✅📦 Продано позавчера -   {get_satat[1][index]} шт.\n'
                                    f'̶̶🚀💵  Продано вчера -   {get_satat[2][index]} шт.\n'
                                    f'📉̶̶  Разница продаж -   {get_satat[3][index]} шт.\n'
                                    f'📉  Процент разницы -   {satat} %\n'
                                    f'Магазин -- {get_satat[6][index]}'.format(message.from_user))
            await bot.send_message(message.from_user.id, "Успешная рассылка")
        except Exception as ex:
                logging.exception(ex)
                await message.answer("Возникла ошибка. Попробуйте еще раз сделать запрос.")
    await bot.send_message(message.from_user.id, "Рассылка завершина")
    
@dp.message_handler(text="sales")
async def get_no_sales_wb(message: types.Message):
    get_satat = get_satat_wb()
    for item_id_user in get_satat[6]:
        try:
            for index, satat in enumerate(get_satat[0]):
                await bot.send_message(item_id_user,
                                    f'Артикул - {get_satat[1][index]}\n'
                                    f'̶̶🤑  Название - {get_satat[2][index]}\n'
                                    f'💰̶̶  На складах {get_satat[3][index]} шт.\n'
                                    f'💸̶̶  Продано за неделю {get_satat[4][index]}\n'
                                    f'💵  Ссылка: {get_satat[5][index]}\n'
                                    f'Магазин -- {get_satat[7][index]}'.format(message.from_user))
            await bot.send_message(message.from_user.id, "Успешная рассылка")
        except Exception as ex:
                logging.exception(ex)
                await message.answer("Возникла ошибка. Попробуйте еще раз сделать запрос.")
    await bot.send_message(message.from_user.id, "Рассылка завершина")
        
        
@dp.message_handler(text="prov")
async def get_add_provider_wb(message: types.Message):
    get_add_stocks = created_xlsx_user_provider()
    for id in get_add_stocks:
        try:
            await bot.send_document(chat_id=id, document=open("Рекомендация по заказу товаров у поставщика.xlsx", 'rb'))
            await bot.send_message(message.from_user.id, "Успешная рассылка")
        except Exception as ex:
            logging.exception(ex)
            await message.answer("Возникла ошибка. Попробуйте еще раз сделать запрос.")
        # await os.remove(get_add_stocks[1])
        time.sleep(0.3)
    await bot.send_message(message.from_user.id, "Рассылка завершина")
    
@dp.message_handler(text="stocks")
async def get_add_stocks_wb(message: types.Message):
    get_add_stocks = created_xlsx_user_provider()
    for id in get_add_stocks:
        try:
            await bot.send_document(chat_id=id, document=open("Нехватка товара на складах.xlsx", 'rb'))
            await bot.send_message(message.from_user.id, "Успешная рассылка")
        except Exception as ex:
            logging.exception(ex)
            await message.answer("Возникла ошибка. Попробуйте еще раз сделать запрос.")
    # await os.remove(get_add_stocks[1][index_id])
        time.sleep(0.3)
    await bot.send_message(message.from_user.id, "Рассылка завершина")  
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)