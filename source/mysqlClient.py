import mysql.connector

# Input = configDetails
# Output = DB connection
# Get the DB details from configDetails
# Connect to Database
# Return connection
# End

def connect_mysql_database(configDetails,logger):
  try:
    mydb = mysql.connector.connect(
      host=configDetails.get("mysql","host").strip(),
      user=configDetails.get("mysql","user").strip(),
      password=configDetails.get("mysql","password").strip(),
      database=configDetails.get("mysql","database").strip()
    )
  except mysql.connector.Error as error:
    logger.error("DB Connection failed, reason is {} ".format(error) )
  except Exception as error:
    logger.error("DB Connection failed, reason is {} ".format(error))
  else:
    logger.info("DB Connection successful")
    return mydb


def insert_into_customer(configDetails,logger,dbConn):
  try:
    logger.info("Start of insert_into_customer")
    thisCursor = dbConn.cursor()
    insertStatement = configDetails.get("customer-insert", "sql-insert").strip()
    val = ("Ashutosh", "Bangalore, 560037")
    thisCursor.execute(insertStatement, val)
  except Exception as error:
    logger.error("Insert operation failed, reason is {} ".format(error))
  else:
    logger.info("Insert operation successful")
    dbConn.commit()
  finally:
    logger.info("End of insert_into_customer")


def update_customer(configDetails,logger,dbConn):
  try:
    logger.info("Start of update_customer")
    thisCursor = dbConn.cursor()
    updateStatement = configDetails.get("customer-update", "sql-update").strip()
    val = ("Bangalore, 560038","Ashutosh")
    thisCursor.execute(updateStatement, val)
  except Exception as error:
    logger.error("Update operation failed, reason is {} ".format(error))
  else:
    logger.info("Update operation successful")
    dbConn.commit()
  finally:
    logger.info("End of update_customer")



def delete_customer(configDetails,logger,dbConn):
  try:
    logger.info("Start of delete_customer")
    thisCursor = dbConn.cursor()
    deleteStatement = configDetails.get("customer-delete", "sql-delete").strip()
    logger.info("deleteStatement = {} ".format(deleteStatement))
    val = ("Ashutosh",)
    thisCursor.execute(deleteStatement, val)
  except Exception as error:
    logger.error("Delete operation failed, reason is {} ".format(error))
  else:
    logger.info("Delete operation successful")
    dbConn.commit()
  finally:
    logger.info("End of delete_customer")


def get_customer(configDetails,logger,dbConn):
  try:
    logger.info("Start of get_customer")
    thisCursor = dbConn.cursor()
    spName = configDetails.get("customer-get", "get_sp").strip()
    logger.info("Procedure Name = {} ".format(spName))
    agrs = [2]
    result = thisCursor.callproc(spName, agrs)

    for result in thisCursor.stored_results():
      records = result.fetchall()
      if len(records) == 0:
        print('Empty table')
      else:
        # print results
        print('Printing Customer details')
        print('----------------------------')
        for record in records:
          print('Id = {}, Name = {}, Address = {}, Gender = {} , Age = {} , lat = {} , lon = {} , bonusPoint = {} , remark = {}'
                .format(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8]))

  except Exception as error:
    logger.error("Get operation failed, reason is {} ".format(error))
  else:
    logger.info("Get operation successful")
    dbConn.commit()
  finally:
    logger.info("End of get_customer")