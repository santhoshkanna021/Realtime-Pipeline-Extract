import pandas as pd
from sqlalchemy import create_engine



#-----AWS Details------------#


username = "postgres"
password = "Quotes2026"
database = "postgres"
host = "quotes-db.cdi2ukwwsds8.ap-south-1.rds.amazonaws.com"
port =  "5432"


#-----------------Create Connection----------#

engine = create_engine( 
    f"postgresql://{username}:{password}@{host}:{port}/{database}"
)


#---------------------------Check the database-----------------#


df = pd.read_sql("Select * from quotes_table" , engine)

print(df.head())