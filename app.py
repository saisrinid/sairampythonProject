from config import DB_DETAILS
import sys


def main():
    env=sys.argv[1]
    db_details=DB_DETAILS[env]
    print(db_details)


if __name__ == '__main__':
    main()