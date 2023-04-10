import pandas as pd
from sqlalchemy import create_engine
import os
import psycopg2
from decouple import config

HOST     = config('HOST')
DATABASE = config('DATABASE')
USER     = config('USER')
PASSWORD = config('PASSWORD')
PORT     = config('PORT')

string_conexao = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
conn_olist = create_engine(string_conexao)

# Inserindo valores nas tabelas com o Pandas

lista = os.listdir('data')

for csv in lista:
    df_order_reviews = pd.read_csv('data/'+csv)
    df_order_reviews.to_sql(csv.replace('_database.csv','').replace('olist_',''), conn_olist, if_exists='replace', index=False)


