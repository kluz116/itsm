from sqlalchemy import create_engine

engine = create_engine('mssql+pyodbc://{user}:{pw}@192.168.0.xxx/{db}?driver=ODBC Driver 17 for SQL Server'.format(user="77777",pw="888888",db="88888"))