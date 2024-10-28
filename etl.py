import os
import pandas as pd
from sqlalchemy import create_engine

# 1. Extract: Read data from a CSV or Excel file
def extract(file_path):
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
            print(f"Extracted data from CSV file: {file_path}")
        elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
            df = pd.read_excel(file_path, engine='openpyxl')
            print(f"Extracted data from Excel file: {file_path}")
        else:
            raise ValueError(f"Unsupported file type: {file_path}")
        
        return df
    except Exception as e:
        print(f"Error extracting data from {file_path}: {e}")
        return None

def transform_clients(df):
    try:
        df_clean = df.dropna(subset=['name', 'email'])
        df_clean['name'] = df_clean['name'].str.upper()        
        print("Clients data transformed successfully.")
        return df_clean
    except Exception as e:
        print(f"Error transforming clients data: {e}")
        return None


    
def transform_transactions(df):
    try:
        df_clean = df.dropna(subset=['client_id', 'transaction_id'])
        df_clean['transaction_date'] = pd.to_datetime(df_clean['transaction_date'], 
                                                       errors='coerce', 
                                                       format='%d/%m/%Y %I:%M:%S %p')
        df_clean = df_clean.dropna(subset=['transaction_date'])

        df_clean['transaction_date'] = df_clean['transaction_date'].dt.strftime('%Y-%m-%d %H:%M:%S')

        print("Transactions data transformed successfully." + df_clean['transaction_date'])
        return df_clean
    except Exception as e:
        print(f"Error transforming transactions data: {e}")
        return None

 
def load(df, db_name, table_name, user, password, host='localhost', port=5432):
    try:
        engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')
        
        df.to_sql(table_name, con=engine, if_exists='append', index=False)
        
        print(f"Data loaded successfully into {table_name} table.")
    except Exception as e:
        print(f"Error loading data: {e}")


def run_etl(file_clients, file_transactions, db_name, user, password):
    clients_data = extract(file_clients)
    if clients_data is not None:
        transformed_clients = transform_clients(clients_data)
        if transformed_clients is not None:
            load(transformed_clients, db_name, 'clients', user, password)

    transactions_data = extract(file_transactions)
    if transactions_data is not None:
        transformed_transactions = transform_transactions(transactions_data)
        if transformed_transactions is not None:
            load(transformed_transactions, db_name, 'transactions', user, password)

if __name__ == "__main__":
    file_clients = 'C:/Users/kifahnaim/Desktop/etlprojectpython/clients.csv'
    file_transactions = 'C:/Users/kifahnaim/Desktop/etlprojectpython/transactions.xlsx'
    
    database_name = 'postgres'
    user = 'postgres'
    password = 'admin'
    
    run_etl(file_clients, file_transactions, database_name, user, password)
