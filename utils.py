import pandas as pd
from mysql import connector as mc
from mysql.connector import errorcode as ec
#import psycopg2 as psy


def get_mysql_conn(DB_USER,DB_PASS,DB_HOST,DB_NAME):
    try:
        conn=mc.connect(user=DB_USER,
                        password=DB_PASS,
                        host=DB_HOST,
                        database=DB_NAME)
    except mc.Error as error:
        if error.errno==ec.ER_ACCESS_DENIED_ERROR:
            print('Invalid Credentials')
        else:
            print(error)
    return conn

#def get_postgres_conn(DB_USER,DB_PASS,DB_HOST,DB_NAME):
#    try:
#        conn=psy.connect(user=DB_USER,
#                        password=DB_PASS,
#                        host=DB_HOST,
#                        database=DB_NAME)
#    except mc.Error as error:
#        if error.errno==ec.ER_ACCESS_DENIED_ERROR:
#            print('Invalid Credentials')
#        else:
#            print(error)
#    return conn
#
#def get_connection(DB_TYPE,DB_USER,DB_PASS,DB_HOST,DB_NAME):
#    if DB_TYPE=='mysql':
#        conn=get_mysql_conn(DB_USER,DB_PASS,DB_HOST,DB_NAME)
#    elif DB_TYPE=='postgres':
#        conn=get_postgres_conn(DB_USER,DB_PASS,DB_HOST,DB_NAME)
#
#    return conn
#
#
#
#
def get_tables(path):
    table_list=pd.read_csv(path,sep=':')
    tables=table_list.loc[table_list['loaded']=='yes','table_name']
    return tables

