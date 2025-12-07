import logging
# from config.config_loader import config_process

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    level= logging.ERROR,
    filename='ERROR.log'
    )

def exception_log(e):
    logging.error(e)
    # config = config_process()
    # verbose = config.get("verbose", False) #False python o false JSON be moshkel nemikhoran chon json.load(f) zadim
    # if verbose == True:
    #     print(e)
