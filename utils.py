import pandas as pd


def get_tables(path):
    table_list=pd.read_csv(path,sep=':')
    tables=table_list.loc[table_list['loaded']=='yes','table_name']
    return tables

