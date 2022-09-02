import datetime
import pandas as pd
from pathlib import Path
from dateutil.relativedelta import relativedelta

pd.set_option('max_columns', None)  # displays all columns
pd.set_option("max_rows", None)     # displays all rows ... change None to 100 ow whatever number
pd.set_option('display.width', 1000)


df = pd.read_csv((Path(r'C:\Users\212628255\Documents\2 GE\AssetPlus\7 Projects\20220831 - Replacement and Exp End Life Fix') / 'REPLACEMENT_FIX (2).csv'))
# print(df)

def do_sql(n_imma, mhs, eqamtcom):
    sql = f"UPDATE B_EQ1996 SET MHS = '{mhs}', EQ_AMT_COM = {eqamtcom} WHERE N_IMMA = '{n_imma}'"
    return sql

def convert_date(d):
    return datetime.datetime.strptime(d,'%Y-%m-%d').date()


cnt = 0

for idx, row in df.iterrows():
    ap = row.N_IMMA
    cneh = row['CNEH']
    try:
        install = convert_date(row.MES1)
        mhs = install + relativedelta(years=int(cneh))
        eq_amt = int(cneh)
        sql = do_sql(ap, mhs, eq_amt)
        print(f"-- Install = {install} plus {eq_amt}")
        print(sql)
        cnt += 1
    except:
        print(f"**************** Error {ap, row.MES1}")

print(f"Total updates = {cnt}")
