from utils import get_mysql_conn
from mysql import connector as mc

def write_data(tgt_db,src_db,table_name):
    conn=mc.connect(user=tgt_db['DB_USER'],
                    password=tgt_db['DB_PASS'],
                    host=tgt_db['DB_HOST'],
                    database=tgt_db['DB_NAME']
                    )
    cursor=conn.cursor()
    src_db_name=src_db['DB_NAME']
    query= f'insert into {table_name} select * from {src_db_name}.{table_name}'
    cursor=conn.cursor()
    cursor.execute(query)
    conn.commit()

    conn.close()