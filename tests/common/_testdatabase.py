from tests.common.database_connector import DatabaseConnector

databaseConnector = DatabaseConnector(host='36.189.234.237', user='lumi', password='6block666', db_name='lumi')
databaseConnector.connect()
databaseConnector.execute_query("select * from ai_device")