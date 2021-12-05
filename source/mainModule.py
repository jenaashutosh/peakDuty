import logging
import sys
import configparser
import mysqlClient as mc

if __name__ == '__main__':
    try:
        logging.basicConfig(stream=sys.stdout, format='%(asctime)s: %(levelname)s - %(message)s',
                            datefmt='%m %d %Y %I:%M:%S %p', level=logging.INFO)
        logger = logging.getLogger()

        logger.info('In Main Program')
        logger.info('Reading config file')
        configDetails = configparser.RawConfigParser()
        configDetails.read("peakduty.config")
        logger.info('Connecting to Database')
        dbConn = mc.connect_mysql_database(configDetails=configDetails,logger=logger)
        if bool(dbConn):
            logger.info(dbConn.get_server_info())
            #mc.insert_into_customer(configDetails=configDetails,logger=logger,dbConn=dbConn)
            #mc.update_customer(configDetails=configDetails, logger=logger, dbConn=dbConn)
            #mc.delete_customer(configDetails=configDetails, logger=logger, dbConn=dbConn)
            mc.get_customer(configDetails=configDetails, logger=logger, dbConn=dbConn)
    except Exception as e:
        logger.error("Error ", str(e))
    else:
        logger.info("Execution Completed")
    finally:
        if bool(dbConn):
            dbConn.close()


