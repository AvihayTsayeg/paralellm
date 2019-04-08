print(__file__)

def print_data(logger, message):
    logger.info(__file__)
    from printer.walla.dalla import print_data_walla
    print_data_walla(logger=logger, message=message)

def get_name():
    return __file__