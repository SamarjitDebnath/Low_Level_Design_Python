from abc import ABC, abstractmethod
from typing import Optional


class LogProcessor(ABC):
    INFO: int = 1
    DEBUG: int = 2
    ERROR: int = 3

    def __init__(self, logProcessor: Optional['LogProcessor'] = None):
        self.nextLogProcessor: Optional['LogProcessor'] = logProcessor

    @abstractmethod
    def process_log(self, logLevel: int, logMessage: str):
        if self.nextLogProcessor != None:
            self.nextLogProcessor.process_log(logLevel, logMessage)
