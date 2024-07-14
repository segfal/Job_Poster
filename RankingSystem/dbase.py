import psycopg2 as pg
from dotenv import load_dotenv
import os
import json
import time
load_dotenv()


DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")



conn = pg.connect(
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    host=DB_HOST,
    port=DB_PORT
)



def create_table(server_name):
    cur = conn.cursor()
    cur.execute(f'''CREATE TABLE IF NOT EXISTS server_name{str(server_name)}(
        id SERIAL PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        date_applied TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        company_name VARCHAR(255) NOT NULL,
        company_position VARCHAR(255) NOT NULL,
        did_apply BOOLEAN DEFAULT FALSE,
        did_interview BOOLEAN DEFAULT FALSE,
        offer varchar(255) DEFAULT 'No Offer')''')
    conn.commit()
    


def insert_data(server_name, username, company_name, company_position):
    cur = conn.cursor()
    cur.execute(f'''INSERT INTO server_name{str(server_name)}(username, company_name, company_position)
    VALUES('{username}', '{company_name}', '{company_position}')''')
    conn.commit()
    print('Data inserted successfully')
    cur.close()

## get ten users that appplied to the most companies
def get_top_ten(server_name):
    cur = conn.cursor()
    cur.execute(f'''SELECT username, COUNT(company_name) FROM server_name{str(server_name)}
    GROUP BY username
    ORDER BY COUNT(company_name) DESC
    LIMIT 10''')
    data = cur.fetchall()
    return data

def get_user_data(server_name, username):
    cur = conn.cursor()
    cur.execute(f'''SELECT * FROM server_name{str(server_name)}
    WHERE username = '{username}' ''')
    data = cur.fetchall()
    return data


def update_data(server_name, username, company_name, company_position, did_apply, did_interview, offer):
    cur = conn.cursor()
    cur.execute(f'''UPDATE server_name{str(server_name)}
    SET did_apply = {did_apply}, did_interview = {did_interview}, offer = '{offer}'
    WHERE username = '{username}' AND company_name = '{company_name}' AND company_position = '{company_position}' ''')
    conn.commit()
    print('Data updated successfully')
    cur.close()

def delete_data(server_name, username, company_name, company_position):
    cur = conn.cursor()
    cur.execute(f'''DELETE FROM server_name{str(server_name)}
    WHERE username = '{username}' AND company_name = '{company_name}' AND company_position = '{company_position}' ''')
    conn.commit()
    print('Data deleted successfully')
    cur.close()

def get_all_data(server_name):
    cur = conn.cursor()
    cur.execute(f'''SELECT * FROM server_name{str(server_name)}''')
    data = cur.fetchall()
    return data


