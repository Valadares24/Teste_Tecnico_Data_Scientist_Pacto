import pandas as pd
import requests

def extract_data(endpoint):
    response = requests.get(f"https://fakestoreapi.com/{endpoint}")
    return response.json()

#extrair
users_raw = extract_data("users")
products_raw = extract_data("products")
carts_raw = extract_data("carts")

#Processar os dados(users)
users_df = pd.json_normalize(users_raw)
users_df = users_df[['id', 'email', 'username', 'password', 'name.firstname', 'name.lastname', 'address.city']]

#prcessar produtos
products_df = pd.DataFrame(products_raw)
produtcst_df = products_df[['id', 'title', 'price', 'description', 'category']]

#processar carrinho
carts_df = pd.DataFrame(carts_raw)
fato_df = carts_df.explode('products').reset_index(drop=True)

#normalizar os dados do carrinho
products_info = pd.json_normalize(fato_df['products'])
fato_df = pd.concat([fato_df.drop(columns=['products']), products_info], axis=1)

#tratamento 
fato_df['date'] = pd.to_datetime(fato_df['date'])
fato_df.rename(columns={'productId': 'product_id','userId': 'user_id'}, inplace=True)

#persistência
users_df.to_csv('users.csv', index=False)
products_df.to_csv('products.csv', index=False)
fato_df.to_csv('fato.csv', index=False)

print("etl concluído com sucesso!")
