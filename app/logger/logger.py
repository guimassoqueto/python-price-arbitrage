from sys import stdout
import logging


def get_logger(name: str):
    """
    Returns a logger object with the specified name.

    Parameters:
    name (str): The name of the logger.

    Returns:
    logger (logging.Logger): The logger object.

    """
    formatter = logging.Formatter('%(asctime)s [%(name)s] %(levelname)s - %(message)s')
    logger_handler = logging.StreamHandler(stdout)
    logger_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logger_handler)

    return logger
