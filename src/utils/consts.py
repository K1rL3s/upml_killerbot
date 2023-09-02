import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()


class Config:
    TOKEN = os.environ["TOKEN"]
    VOLUME_FOLDER = (
        Path(__file__).absolute().parent.parent / "database" / "db_files"
    )
    DB_FILE = VOLUME_FOLDER / (os.getenv("DB_FILE") or "database.sqlite")
    LOG_FILE = VOLUME_FOLDER / (os.getenv("LOG_FILE") or "logs.log")
    BETTER_CALL_SAUL = (
        os.getenv("BETTER_CALL_SAUL")
        or "Если возникнут вопросы, спрашивайте в беседе потоков без учителей"
    )

    ADMINS = tuple(
        [
            int(os.environ[key])
            for key in os.environ.keys()
            if key.startswith("ADMIN") and os.environ[key].isdigit()
        ]
    )


class CallbackData:
    JOIN_THE_GAME = "join_the_game"


class TextCommands:
    CONFIRM_DEATH = "Подтвердить смерть☠️"
    REMIND_VICTIM = "Напомнить цель🔪"
    YES = "Да"
    NO = "Нет"


MESSAGE_WIDTH_LIMIT = 4096  # telegram limit
TG_ID = int  # для аннотаций
DB_ID = int  # для аннотаций

WELCOME = f"""Привет, это бот игры "Киллер". 
Каждый год в ЮФМЛ проводится эта игра для общего знакомства. Цель игры - "убить" свою цель, получить новую и так по кругу.

Для того чтобы "убить" нужно выполнить следующие условия:

- Вы со своей жертвой должны находиться полностью одни в одном помещении (кабинет, комната общежития, кухня и т.д.).

- Нельзя "убивать" в туалете и в душевой ОБЩЕЖИТИЯ. В лицее можно "убивать" везде.

- "Убивать" можно только с 8:30 до 22:00

- Вы должны сказать свой жертве: "Бордовая львица кушает пиццу"

- Нельзя трогать жертву или применять насилие ради "убийства".

- После "убийства" жертва должна в боте нажать на кнопку "Подтвердить смерть", после "убийца" сразу получит новую цель.

- Игра идёт до того момента, пока в игре не останется 2 человека - они становятся победителями.

- {Config.BETTER_CALL_SAUL}"""

LETS_PLAY_BUTTON = "🩸Участвовать"
READ_NAME_1 = """Введите свою фамилию и имя (например, "Иванов Иван", без кавычек).
Всех участников проверят на корректность имени, и если вы введёте что-то другое, то вас исключат из игры."""
READ_NAME_2 = """Вы успешно зарегистрированы! 
Если вы ввели имя неправильно, дождитесь удаления вас из участников или сразу обратитесь к администратору (последнее предложение /start)"""
NAME_ALREADY_EXISTS = "Вы уже участвуете в игре или такое имя занято."
GAME_ALREADY_STARTED = "Игра уже началась, вы не можете присоединиться."
ARE_YOU_SURE_DEATH_CONFIRM = "Вы уверены, что хотите подтвердить смерть?"
YOU_ARE_DEAD = "Вы мертвы."
ALREADY_DEAD = "Вы уже мертвы."
DEATH_CONFIRMED = "Вы погибли."
DELETED = "Вы были удалены из игры."
