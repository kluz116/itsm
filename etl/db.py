import pyodbc

try:
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.0.180;PORT=1433;DATABASE=FinAnalytics;UID=realm;PWD=friend;TDS_Version=8.0;MARS_Connection=Yes;')
except Exception as e:
    print(e)
