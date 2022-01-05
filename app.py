from config import DB_DETAILS
import sys
from utils import get_tables
from read import fetch_recs
from write import write_data





def main():
    env=sys.argv[1]
    db_details=DB_DETAILS[env]
    src_db=db_details['SOURCE_DB']
    tgt_db=db_details['TARGET_DB']

    tables=get_tables('table_list.txt')
    for table in tables:
        #data,column_names=fetch_recs(src_db,table,5)
        #for rec in data:
            #print(rec)
        write_data(tgt_db,src_db,table)



if __name__ == '__main__':
    main()