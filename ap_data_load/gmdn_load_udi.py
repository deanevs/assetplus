import pandas as pd
import re
import sql_mapping
import pyodbc
import sys

pd.set_option('max_columns', None)
pd.set_option("max_rows", None)
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', 1000)

def main():
    # get our db connection to Assetplus
    conn = pyodbc.connect("DSN=PYTHON_UDI")
    cursor = conn.cursor()

    # now we have that, we need to load the excel file
    fn = "C:\\Users\\212628255\\Documents\\GE\\AssetPlus\\7 Projects\\GMDN\\GMDN_TERMS.xlsx"
    df = pd.read_excel(fn)

    sql_create_table = "CREATE TABLE GMDN_TERMS (" \
                       "GMDN_CODE nvarchar(10)," \
                       "TERM_NAME nvarchar(100)," \
                       "GMDN_DEFINITION nvarchar(1024)," \
                       "STATUS nvarchar(50)," \
                       "IS_IVD nvarchar(50)," \
                       "CREATED_DATE date)"

    cursor.execute(sql_create_table)
    conn.commit()


    cnt = 0
    for index, row in df.iterrows():
        # if row['STATUS'] == 'Obsolete':
        #     continue
        record = (str(row['GMDN_CODE']), row['TERM_NAME'], row['GMDN_DEFINITION'], row['STATUS'], row['IS_IVD'], row['CREATED_DATE'])
        cursor.execute("INSERT INTO GMDN_TERMS (GMDN_CODE, TERM_NAME, GMDN_DEFINITION, STATUS, IS_IVD, CREATED_DATE) VALUES (?,?,?,?,?,?)", record)
        cnt += 1
    conn.commit()

    print("Inserted {} rows".format(str(cnt)))


if __name__ == "__main__":
    main()
