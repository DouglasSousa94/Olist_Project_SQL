#  Dataset Disponibilizado pela Olist"

import pandas as pd

!pip install psycopg2
!pip install sqlalchemy
from sqlalchemy import create_engine

string_conexao = 'postgresql://postgres:DS2022@localhost:5432/Olist'
conn_olist = create_engine(string_conexao)

# Inserir valores nas tabelas com o Pandas

df_customers = pd.read_csv("Data/olist_customers_dataset.csv")
df_customers.to_sql("customers", conn_olist, if_exists="replace")

df_geolocation = pd.read_csv("Data/olist_geolocation_dataset.csv")
df_geolocation.to_sql("geolocation", conn_olist, if_exists="replace")

df_order_items = pd.read_csv("Data/olist_order_items_dataset.csv")
df_order_items.to_sql("order_items", conn_olist, if_exists="replace")

df_order_payments = pd.read_csv("Data/olist_order_payments_dataset.csv")
df_order_payments.to_sql("order_payments", conn_olist, if_exists="replace")

df_order_reviews = pd.read_csv("Data/olist_order_reviews_dataset.csv")
df_order_reviews.to_sql("order_reviews", conn_olist, if_exists="replace")

df_orders = pd.read_csv("Data/olist_orders_dataset.csv")
df_orders.to_sql("orders", conn_olist, if_exists="replace")

df_products = pd.read_csv("Data/olist_products_dataset.csv")
df_products.to_sql("products", conn_olist, if_exists="replace")

df_sellers = pd.read_csv("Data/olist_sellers_dataset.csv")
df_sellers.to_sql("sellers", conn_olist, if_exists="replace")

df_product_category_name_translation = pd.read_csv("Data/product_category_name_translation.csv")
df_product_category_name_translation.to_sql("product_category_name_translation", conn_olist, if_exists="replace")

