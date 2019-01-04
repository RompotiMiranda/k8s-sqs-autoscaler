import logging
import os, sys
from logging.handlers import TimedRotatingFileHandler
from logging import StreamHandler

logger = None


def setup_logging(options):
    global logger
    """Set up logging file handler for both app and sqs consumer"""
    file_handler = TimedRotatingFileHandler("logs/autoscaling.log", "D", 1, 10)
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]")
    )
    stream_handler = StreamHandler(sys.stdout)
    stream_handler.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
    logger = logging.getLogger("autoscaling")
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    logger.setLevel(options.log_level)
