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
    conn_udi = pyodbc.connect("DSN=PYTHON_UDI")
    conn_ap = pyodbc.connect(("DSN=PYTHON_SQL"))
    cursor_udi = conn_udi.cursor()
    cursor_ap = conn_ap.cursor()


    # empty manufacturer table to start again
    cursor_ap.execute("TRUNCATE TABLE MARQUES")
    conn_ap.commit()

    # get uniques manufacturers from UDI
    df_man_udi = pd.read_sql_query("SELECT DISTINCT CompanyName FROM tbl_Device", conn_udi)

    man_series = pd.Series(df_man_udi['CompanyName'])
    man_series = man_series.str[0:50].str.upper()
    # print(man_series.shape)
    # sys.exit()

    sql = "INSERT INTO MARQUES ([MA_NOM]) VALUES (?)"

    cnt = 0
    try:
        for company in man_series:
            cursor_ap.execute(sql, company)
            cnt += 1
    except pyodbc.DatabaseError as err:
        print(err)
        conn_ap.rollback()
    else:
        conn_ap.commit()
    finally:
        print("Added {} companies".format(cnt))

if __name__ == "__main__":
    main()
