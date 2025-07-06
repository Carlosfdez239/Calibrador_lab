import logging

def configurar_logger(modo="debug"):
    logger = logging.getLogger("noria")
    logger.setLevel(logging.DEBUG if modo == "debug" else logging.INFO)

    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

    file_handler = logging.FileHandler("noria.log")
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    logger.handlers = []  # Limpia handlers previos
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger