from log_processor.logProcessor import LogProcessor


class DebugLogProcessor(LogProcessor):
    def __init__(self, nextProcessor: LogProcessor | None = None):
        super().__init__(nextProcessor)

    def process_log(self, logLevel, logMessage):
        if logLevel == LogProcessor.DEBUG:
            print(f"[DEBUG] - {logMessage}")
        else:
            super().process_log(logLevel, logMessage)
