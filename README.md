# Anverali Group Test Task

---

TG Бот, который создает задачи через /add и добавляет их в БД PostgreSQL. Также по команде /tsk выводит список задач из БД.

## Установка проекта

---

Клонируйте репозиторий  

Активируйте виртуальное окружение  

```bash
poetry shell
```


Установите зависимости  
```bash
poetry install
```

Получите TOKEN телеграм в BotFather

Создайте БД

Создайте в корне проекта файл .env и внесите в него все переменные окружения по образцу из файла .env.sample

Запустите проект  
```bash
python main.py
```

### Стэк

---


- Python 3.12
- python-telegram-bot 21.1.1
- БД: PostgreSQL
- SQLAlchemy


