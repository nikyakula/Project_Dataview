import pyodbc
server = 'mssql-clo-prod.c0cqs7rsnqyl.us-east-1.rds.amazonaws.com'
database = 'clo_factorydb'
username = 'clowebuser'
password = 'R8b}EtjgP$n_H'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT batchID FROM rawload.batchException;")
rows = cursor.fetchall()
for row in rows:
    print (row.batchID) 


