import logging

from telegram import Update
from telegram.ext import CallbackContext

from src.db import SessionLocal
from src.models import Task

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        'Привет ! Я бот-помощник для управления задачами.\nВведите /add чтобы добавить задачу.'
        '\nВведите /tsk чтобы посмотреть список задач'
    )


async def add_task(update: Update, context: CallbackContext) -> None:
    with SessionLocal() as session:
        task_text = ' '.join(context.args)

        if task_text:
            task = Task(task_text=task_text)
            session.add(task)
            session.commit()
            await update.message.reply_text('Задача успешно добавлена!')
        else:
            await update.message.reply_text('Использование: /add <текст задачи>')


async def list_tasks(update: Update, context: CallbackContext) -> None:
    with SessionLocal() as session:
        tasks = session.query(Task).all()
        task_list = '\n'.join([f'{task.id}. {task.task_text}' for task in tasks])
        await update.message.reply_text(f'Список задач:\n{task_list}')
