from config import DB_DETAILS
import sys
from utils import get_tables


def main():
    env=sys.argv[1]
    db_details=DB_DETAILS[env]
    #print(db_details)
    tables=get_tables('table_list.txt')
    for table in tables:
        print(table)



if __name__ == '__main__':
    main()