from log_processor.logProcessor import LogProcessor


class ErrorLogProcessor(LogProcessor):
    def __init__(self, nextProcessor: LogProcessor | None = None):
        super().__init__(nextProcessor)

    def process_log(self, logLevel, logMessage):
        if logLevel == LogProcessor.ERROR:
            print(f"[ERROR] - {logMessage}")
        else:
            super().process_log(logLevel, logMessage)
