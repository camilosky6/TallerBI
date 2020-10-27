import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import requests

#Name of file
name_file = 'C:/Users/joshu/Desktop/Universidad/Semestre 8/BI/Casos_positivos_de_COVID-19_en_Colombia.csv'

#Read csv file with pandas
data_df = pd.read_csv(name_file, header=0, encoding='UTF_8', delimiter=',')

#Understand the data [First Look]
print("First data in dataframe: \n %s" %data_df.head(2))
print("List of data types in dataframe: \n %s" %data_df.dtypes)


# Select columns to load on DB
data_to_db = data_df[['ID de caso', 'Fecha de notificación']]

print(data_to_db)


# Load to DB
engine = create_engine('postgresql://postgres:123@127.0.0.1:5432/postgres')
data_to_db.to_sql('covid_data_from_python', con=engine, index=False, if_exists='replace')

CLIENT_ID = 'afecd61eb20d4d4ea519f7a55046effe'
CLIENT_SECRET = '4b5ce10bafa04a3f88456aee36bad454'

AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']