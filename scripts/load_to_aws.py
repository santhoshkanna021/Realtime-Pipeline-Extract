import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# ----------------- Load .env ----------------- #
load_dotenv()

# ----- AWS / Database Details from .env ----- #

username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")  

# ----------------- Create Connection ----------------- #
try:
    engine = create_engine(
        f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
    )
    print("✅ Successfully connected to AWS RDS...")
except Exception as e:
    print("❌ Connection failed:", e)
    exit(1)

# ----------------- Load Data into Database ----------------- #
try:
    df = pd.read_csv("scripts/data/clean_dataset.csv") 
    df.to_sql("quotes_table", engine, if_exists="replace", index=False)
    print("✅ Data uploaded successfully to AWS RDS!")
except Exception as e:
    print("❌ Failed to upload data:", e)