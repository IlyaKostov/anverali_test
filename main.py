import logging
import os

from telegram.ext import CommandHandler, ApplicationBuilder

from src.db import Base, engine
from src.handlers import start, list_tasks, add_task


TOKEN = os.getenv('BOT_TOKEN')

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

Base.metadata.create_all(bind=engine)


def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('add', add_task))
    application.add_handler(CommandHandler('tsk', list_tasks))

    application.run_polling()


if __name__ == '__main__':
    main()
