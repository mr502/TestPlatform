import logging
import os
from pathlib import Path

class Logger:
    _instance = None
    def __init__(self, log_file=Path(__file__).parent / "logs" / "pytest.log"
, level=logging.DEBUG):
        # 避免重复初始化
        if hasattr(self, 'logger'):
            return

        # 创建日志记录器
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level)

        # 清理已存在的处理器
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)

        # 创建文件处理器，将日志写入文件
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)

        # 创建控制台处理器，将日志输出到控制台
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)

        # 创建日志格式
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # 将文件处理器添加到日志记录器
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)