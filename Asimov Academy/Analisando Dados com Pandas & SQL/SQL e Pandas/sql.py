import sqlite3
import pandas as pd

conn = sqlite3.connect('web.db')

df_data = pd.read_csv('bd_data.csv', index_col=0)
df_data.index.name = 'index_name'
df_data.to_sql('data', conn, index_label='index_name')

c = conn.cursor()

# c.execute('CREATE TABLE Products (products_id, product_name, price)')

# c.execute('DROP TABLE Products')

c.execute('CREATE TABLE Products ([products_id] INTEGER PRIMARY KEY, [product_name] TEXT, [price] INTEGER)')

# INSERT
c.execute('''INSERT INTO Products (products_id, product_name, price)
    VALUES
    (1, 'Computer', 800),
    (2, 'Printer', 200),
    (3, 'Tablet', 300)
''')
# conn.commit() necessário ocasionalmente para executar o comando SQL.
conn.commit()

# Cria uma tabela a partir da primeira mas selecionando os itens de trás para frente e de 2 em 2.
df_data2 = df_data.iloc[::-2]
df_data2.to_sql('data', conn, if_exists='append')
