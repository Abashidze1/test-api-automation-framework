from loguru import logger

logger.remove()

logger.add("logs/api_tests.log", level="INFO", rotation="1 MB", encoding="utf-8")