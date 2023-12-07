from moduleImporter import *


def main():
    log: LogProcessor = InfoLogProcessor(
        DebugLogProcessor(ErrorLogProcessor(None)))
    log.process_log(LogProcessor.INFO, f"Testing {LogProcessor.INFO} logging")
    log.process_log(LogProcessor.DEBUG,
                    f"Testing {LogProcessor.DEBUG} logging")
    log.process_log(LogProcessor.ERROR,
                    f"Testing {LogProcessor.ERROR} logging")


if __name__ == '__main__':
    main()




