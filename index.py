import pandas as pd
from Regex import RegexClass

def extract_dataset_by_state(df):
    estado_dfs = {estado: df[df['state'] == estado] for estado in df['state'].unique()}

    for estado, df_estado in estado_dfs.items():
        path = f"datasets/datasets_tratadas/logs_{estado}.csv"
        df_estado.to_csv(path, index=False)
        print(f"dataset gerada para o estado de {estado}")


df = pd.read_csv('datasets/MOCK_DATA.csv')
# print(df.to_json())

timestamp = df['timestamp']
user_name = df['name'] 
user_age = df['age']
user_state = df['state'] 
df['gender'] = df['gender'].apply(lambda x: 'M' if x == 'Male' else 'F')
news_id = df['news_id']
time_spent = df['time_spent']
device = df['device']

news = [
    "news/1.txt",
    "news/2.txt",
    "news/3.txt",
    "news/4.txt",
    "news/5.txt",
    "news/6.txt",
    "news/7.txt",
    "news/8.txt",
    "news/9.txt",
    "news/10.txt",
    "news/11.txt",
    "news/12.txt",
    "news/13.txt",
    "news/14.txt",
    "news/15.txt",
    "news/16.txt",
    "news/17.txt",
    "news/18.txt",
    "news/19.txt",
    "news/20.txt",
]

for index, row in df.iterrows():
    news_id = int(row['news_id']) - 1

    RegexClass().noticia_relacionada_a_esporte(news[news_id])
    # print(response)

# Regex.noticia_relacionada_a_esporte(news, )

# extract_dataset_by_state(df)

