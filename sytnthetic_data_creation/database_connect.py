import yaml
from distutils.log import error
import mysql.connector
import os
import random
import datetime
from dotenv import load_dotenv

from dotenv import load_dotenv

# load enverioment (.env) file
env_path = os.path.join(".env", "./")
load_dotenv()


def mongodb_connection(credentials: dict = None):
    if (credentials):
        mongo_host = credentials['host']
        mongo_port = credentials['port']
        mongo_user = credentials['user']
        mongo_password = credentials['password']
        mongo_collection = credentials['collection']
    else:
        if os.getenv("USE_MONGO") == True:
            mongo_host = os.getenv("MONGO_HOST"),
            mongo_port = os.getenv("MONGO_PORT"),
            mongo_user = os.getenv("MONGO_USER"),
            mongo_password = os.getenv("MONGO_PASSWORD"),
            mongo_database = os.getenv("MONGO_COLLECTION")


def sql_connection(credentials=None):

    if (credentials != None):
        sql_host = credentials['host']
        sql_port = credentials['port']
        sql_user = credentials['user']
        sql_password = credentials['password']
        sql_database = credentials['database']
    else:

        sql_host = "127.0.0.1"
        sql_port = 8889
        sql_user = "dp_lab"
        sql_password = "Rykontech1"
        sql_database = "Health_DP"

    print(sql_host, sql_port, sql_user)
    mydb = mysql.connector.connect(
        host=sql_host,
        port=sql_port,
        user=sql_user,
        password=sql_password,
        database=sql_database
    )
    return mydb
