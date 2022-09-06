import pyodbc

server = 'xxxxxx'
database = 'xxxxxxx'
username = 'xxxxx'
password = 'xxxx'
try:
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

except Exception as e:
    print(e)