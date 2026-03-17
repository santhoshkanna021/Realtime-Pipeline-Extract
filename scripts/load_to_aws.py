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

print("Successfully AWS will be Connected...")


#-----------------Load Data into the CSV------------------#

df = pd.read_csv("scripts/data/clean_dataset.csv")

df.to_sql("quotes_table", engine, if_exists="replace", index=False)

print("Data Upload Successfully")