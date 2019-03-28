

print(__file__)

def print_data(logger, message):
    logger.info(__file__)
    logger.info(locals())
    logger.info(globals())
    from printer.walla.dalla import print_data_walla
    print_data_walla(logger, message)

def get_name():
    return __file__