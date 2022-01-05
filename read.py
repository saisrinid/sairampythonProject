from utils import get_mysql_conn

def fetch_recs(src_db,table_name,limit):

    conn = get_mysql_conn(src_db['DB_USER'], src_db['DB_PASS'], src_db['DB_HOST'], src_db['DB_NAME'])
    if limit==0:
        query= f'select * from {table_name}'
    else:
        query= f'select * from {table_name}  limit {limit}'

    cursor=conn.cursor()
    cursor.execute(query)
    data=cursor.fetchall()
    column_names=cursor.column_names

    conn.close()
    return data,column_names
