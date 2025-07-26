from sqlalchemy import create_engine
from models import Base
import pandas as pd

engine = create_engine('postgresql://chatbot:chatbot@localhost/ecommerce')
Base.metadata.create_all(engine)

# Load each CSV
for table in ['products', 'orders', 'inventory_items']:
    df = pd.read_csv(f'data/{table}.csv')
    df.to_sql(table, engine, if_exists='replace', index=False)
