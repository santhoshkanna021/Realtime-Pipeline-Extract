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
port = os.getenv("DB_PORT", "5432")  # default port if not provided

# ----------------- Create Connection ----------------- #
try:
    engine = create_engine(
        f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
    )
    print("✅ Successfully connected to AWS RDS...")
except Exception as e:
    print("❌ Connection failed:", e)
    exit(1)

# ----------------- Read Data from Database ----------------- #
try:
    df = pd.read_sql("SELECT * FROM quotes_table;", engine)
    print("✅ Data fetched successfully!")
    print(df.head())  # Display first 5 rows
except Exception as e:
    print("❌ Failed to fetch data:", e)