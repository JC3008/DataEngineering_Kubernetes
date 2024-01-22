from datetime  import datetime as dt
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sqlalchemy
import pandas as pd

lat_long = {
    'AC': [ -8.77, -70.55]
  , 'AL': [ -9.71, -35.73]
  , 'AM': [ -3.07, -61.66]
  , 'AP': [  1.41, -51.77]
  , 'BA': [-12.96, -38.51]
  , 'CE': [ -3.71, -38.54]
  , 'DF': [-15.83, -47.86]
  , 'ES': [-19.19, -40.34]
  , 'GO': [-16.64, -49.31]
  , 'MA': [ -2.55, -44.30]
  , 'MT': [-12.64, -55.42]
  , 'MS': [-20.51, -54.54]
  , 'MG': [-18.10, -44.38]
  , 'PA': [ -5.53, -52.29]
  , 'PB': [ -7.06, -35.55]
  , 'PR': [-24.89, -51.55]
  , 'PE': [ -8.28, -35.07]
  , 'PI': [ -8.28, -43.68]
  , 'RJ': [-22.84, -43.15]
  , 'RN': [ -5.22, -36.52]
  , 'RO': [-11.22, -62.80]
  , 'RS': [-30.01, -51.22]
  , 'RR': [  1.89, -61.22]
  , 'SC': [-27.33, -49.44]
  , 'SE': [-10.90, -37.07]
  , 'SP': [-23.55, -46.64]
  , 'TO': [-10.25, -48.25]
}

df_lat = pd.DataFrame(lat_long)
df_long = pd.DataFrame(lat_long)

df_lat = df_lat[:1]
df_long = df_long[1:]

cad = pd.read_csv(r'cad_cia_aberta.csv',sep=';',encoding='utf-8')
dfp_con = pd.read_csv(r'dfp_cia_aberta_DRE_con_2022.csv',sep=';',encoding='Windows-1252')


SERVER = 'DESKTOP-DD8P4JN'
DATABASE = 'B3_DATA_DISCOVERING'
DRIVER = 'SQL Server Native Client 11.0'
USERNAME = 'sa'
PASSWORD = 'jotace007'
DATABASE_CONNECTION = f'mssql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}'
    
engine = create_engine(DATABASE_CONNECTION)
connection = engine.connect()

cad.to_sql('dfp_cad',con=engine,if_exists='replace',index=None)

dfp_con.to_sql('dfp_ind',con=engine,if_exists='replace',index=None)

df_lat.to_sql('latitude_estados',con=engine,if_exists='replace',index=None)
df_long.to_sql('longitude_estados',con=engine,if_exists='replace',index=None)
