import asyncio
import logging
from aiogram import Bot, Dispatcher
from config_data.config import load_config, Config
from handlers import user_handlers, other_handlers
from keyboards.main_menu import set_main_menu

logger = logging.getLogger(__name__)

async def main():

    # initialization of logs
    logging.basicConfig(
        level=logging.INFO, 
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s',
    )

    logging.info('Starting bot')

    # load config
    config: Config = load_config()

    # bot initialization and dispatcher
    bot = Bot(token=config.bot.token, parse_mode='HTML')
    dp = Dispatcher()

    # setting the main menu
    await set_main_menu(bot)

    # registering routers in the dispatcher
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Skipping the accumulated updates and start polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())




