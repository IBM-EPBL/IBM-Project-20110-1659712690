dsn_hostname = "19af6446-6171-4641-8aba-9dcff8e1b6ff.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud" 
dsn_uid = "wkw32408" 
dsn_pwd = "gPv9B5Ma2mjIrRzq" 
dsn_driver = "{IBM DB2 ODBC DRIVER}" 
dsn_database = "BLUDB" # e.g. "BLUDB" 
dsn_port = "30699" # e.g. "32733" 
dsn_protocol = "TCPIP" # i.e. "TCPIP" 
dsn_security = "SSL" #i.e. "SSL"

dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
    "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd,dsn_security) 
print(dsn)
try:
    conn = ibm_db.connect(dsn, "", "") 
    print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)
except:
    print ("Unable to connect: ", ibm_db.conn_errormsg() )

server = ibm_db.server_info(conn)
print ("DBMS_NAME: ", server.DBMS_NAME) 
print ("DBMS_VER: ", server.DBMS_VER) 
print ("DB_NAME: ", server.DB_NAME)
client = ibm_db.client_info(conn)
print ("DRIVER_NAME: ", client.DRIVER_NAME) 
print ("DRIVER_VER: ", client.DRIVER_VER) 
print ("DATA_SOURCE_NAME: ", client.DATA_SOURCE_NAME) 
print ("DRIVER_ODBC_VER: ", client.DRIVER_ODBC_VER) 
print ("ODBC_VER: ", client.ODBC_VER)
print ("ODBC_SQL_CONFORMANCE: ", client.ODBC_SQL_CONFORMANCE)
print ("APPL_CODEPAGE: ", client.APPL_CODEPAGE) 
print ("CONN_CODEPAGE: ", client.CONN_CODEPAGE)

ibm_db.close(conn)