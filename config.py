import os


DB_DETAILS={
    'dev':{
        'SOURCE_DB':{
            'DB_TYPE':'mysql',
            'DB_HOST':'localhost',
            'DB_NAME': os.environ.get('SRC_DB_NAME'),
            'DB_USER': os.environ.get('SRC_DB_USER'),
            'DB_PASS': os.environ.get('SRC_DB_PASS')
        },
        'TARGET_DB':{
            'DB_TYPE':'mysql',
            'DB_HOST':'localhost',
            'DB_NAME': os.environ.get('TGT_DB_NAME'),
            'DB_USER': os.environ.get('TGT_DB_USER'),
            'DB_PASS': os.environ.get('TGT_DB_PASS')
        }
    }
}
