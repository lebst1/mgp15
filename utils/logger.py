import logging
import os
from datetime import datetime

# Определяем путь к папке с логами
LOG_DIR = "logs"

# Создаём папку для логов, если она не существует
# exist_ok=True — не выдаёт ошибку, если папка уже есть
os.makedirs(LOG_DIR, exist_ok=True)

# Настраиваем базовую конфигурацию логирования
logging.basicConfig(
    level=logging.INFO,  # Уровень логирования (INFO, DEBUG, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Формат сообщений
    datefmt='%Y-%m-%d %H:%M:%S',  # Формат даты и времени
    handlers=[
        # Файловый обработчик — логи сохраняются в файл с датой в имени
        logging.FileHandler(
            f'{LOG_DIR}/bot_{datetime.now().strftime("%Y%m%d")}.log',
            encoding='utf-8'  # Поддержка русских символов
        ),
        # Консольный обработчик — логи выводятся в терминал
        logging.StreamHandler()
    ]
)

# Создаём и экспортируем объект логгера
logger = logging.getLogger(__name__)