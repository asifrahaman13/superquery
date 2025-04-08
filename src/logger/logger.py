import logging
from logging.handlers import RotatingFileHandler
import os


class Logger:
    def __init__(self, name: str, level: str = "DEBUG", log_dir: str = "logs"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(getattr(logging, level.upper()))

        if not self.logger.handlers:
            os.makedirs(log_dir, exist_ok=True)
            log_path = os.path.join(log_dir, f"{name}.log")

            file_handler = RotatingFileHandler(
                log_path, maxBytes=5 * 1024 * 1024, backupCount=5
            )
            file_handler.setFormatter(self._formatter())
            self.logger.addHandler(file_handler)

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self._formatter())
            self.logger.addHandler(console_handler)

    def _formatter(self):
        return logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(name)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

    def get_logger(self):
        return self.logger
