import logging


def send_log(message):
    logging.basicConfig(filename="syslog.log", level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')
    try:
        logging.info(message)

    except Exception as e:
        logging.exception("Error! ", str(e))
