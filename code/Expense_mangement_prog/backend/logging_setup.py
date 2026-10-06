import logging

def setup_logger(name):
    #Create a custom logger :
    logger = logging.getLogger('name')

    #configure the custom logger :
    logger.setLevel(logging.DEBUG)
    filehandler = logging.FileHandler('server.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

    return logger