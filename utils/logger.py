import logging

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)  # Set the logging level
    logger.propagate = False  # Prevent propagation to parent loggers
    if not logger.handlers:  # Avoid adding multiple handlers
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    return logger