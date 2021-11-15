
import logging
import sys
import mysqlClient as mc
import pandas as pd
import numpy as np

if __name__ == '__main__':

    logging.basicConfig(stream=sys.stdout, format='%(asctime)s: %(levelname)s - %(message)s',datefmt='%m %d %Y %I:%M:%S %p',level=logging.INFO)
    logger = logging.getLogger()

    logger.info('In Main Program')

    x = 10
    list =[1,2,3,4,5]
    sum = mc.callFunctions(logger,x,list)
    logger.info("Sum %i ", sum)