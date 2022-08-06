import pandas as pd
from dataconnections.destination_database import engine


class Core:

    def read_from_customer_accounts(self, conn):
        try:
            query = "select * from t_CollateralInsurance order by CreatedOn desc"
            result_port_map = pd.read_sql(query, conn)
            df = pd.DataFrame(result_port_map)
            df.to_sql('t_CollateralInsurance', con=engine, if_exists='replace', chunksize=1000)
            print('**Successfully Inserted Data**')

        except Exception as e:
            print(e)