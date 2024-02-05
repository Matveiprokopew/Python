import config
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType

# log
logging.basicConfig(level=logging.INFO)

# init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

# prices
PRICE = types.LabeledPrice(label="Подписка на 1 месяц", amount=500*100)  # в копейках (руб)


# buy
@dp.message_handler(commands=['buy'])
async def buy(message: types.Message):
    if config.PAYMENTS_TOKEN.split(':')[1] == 'TEST':
        await bot.send_message(message.chat.id, "Тестовый платеж!!!")

    await bot.send_invoice(message.chat.id,
                           title="Подписка на бота",
                           description="Активация подписки на бота на 1 месяц",
                           provider_token=config.PAYMENTS_TOKEN,
                           currency="rub",
                           photo_url="https://www.aroged.com/wp-content/uploads/2022/06/Telegram-has-a-premium-subscription.jpg",
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False,
                           prices=[PRICE],
                           start_parameter="one-month-subscription",
                           payload="test-invoice-payload")