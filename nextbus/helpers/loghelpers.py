import logging
import time


# def init_logger():

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
    filename="nextbus.log",
    encoding="utf-8",
    level=logging.INFO)
logger = logging.getLogger('')
    # return logger


def log_success(start_time: int, message=""):
    runtime = time.perf_counter() - start_time
    logger.info("status:%s, runtime:%.4f, %s", "SUCCESS", runtime, message)


def log_failure(start_time: int, message=""):
    runtime = time.perf_counter() - start_time
    logger.error("status:%s, runtime:%.4f, %s", "FAILURE", runtime, message)