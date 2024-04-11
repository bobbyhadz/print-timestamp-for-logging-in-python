# How to print a Timestamp for Logging in Python

import logging
import time

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.info('Info message #1')

time.sleep(2)

logging.info('Info message #2')

time.sleep(2)

logging.debug('Debug message #1')

time.sleep(2)

logging.error('Error message #1')

time.sleep(2)

logging.warning('Warning message #1')

time.sleep(2)

logging.critical('Critical message #1')