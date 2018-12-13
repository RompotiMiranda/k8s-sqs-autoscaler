import logging
import os, sys
from logging.handlers import TimedRotatingFileHandler
from logging import StreamHandler


def setup_logging():
    """Set up logging file handler for both app and sqs consumer"""
    file_handler = TimedRotatingFileHandler("logs/autoscaling.log", "D", 1, 10)
    format_ = "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"
    file_handler.setFormatter(logging.Formatter(format_))
    stream_handler = StreamHandler(sys.stdout)
    stream_handler.setFormatter(logging.Formatter(format_))
    logger_instance = logging.getLogger("autoscaling")
    logger_instance.addHandler(file_handler)
    logger_instance.addHandler(stream_handler)
    level = os.environ.get("LOGGING_LEVEL", "ERROR")
    logger_instance.setLevel(level)
    return logger_instance


logger = setup_logging()
