import sqlite3
import pandas as pd

conn = sqlite3.connect('web.db')

df_data = pd.read_csv('bd_data.csv', index_col=0)
df_data.index.name = 'index_name'
df_data.to_sql('data', conn, index_label='index_name')

c = conn.cursor()
# conn.commit() necessário ocasionalmente para executar o comando SQL.
c.execute('CREATE TABLE Products (products_id, product_name, price)')

c.execute('DROP TABLE Products')

c.execute('CREATE TABLE Products ([products_id] INTEGER PRIMARY KEY, [product_name] TEXT, [price] INTEGER)')
