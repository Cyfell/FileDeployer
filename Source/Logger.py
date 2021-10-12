import logging


log_controller = logging.getLogger('Controller')


# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
log_formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s', datefmt='%I:%M:%S')

# add formatter to ch
ch.setFormatter(log_formatter)

# add ch to logger
log_controller.addHandler(ch)

# set default levels
log_controller.setLevel(logging.INFO)
