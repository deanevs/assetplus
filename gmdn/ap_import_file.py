import pandas as pd
import re
import sql_mapping
import pyodbc
import sys

pd.set_option('max_columns', None)
pd.set_option("max_rows", None)
pd.set_option('display.width', 1000)

def main():
    # get our db connection to Assetplus
    conn = pyodbc.connect("DSN=PYTHON_SQL")
    cursor = conn.cursor()

    # load AssetPlus table into a dataframe
        # df_model = get_ap_table(sql_mapping.sql_model, conn)
        # df_gmdn = get_ap_table(sql_mapping.sql_gmdn, conn)
    df_manufacturer = get_ap_table(sql_mapping.sql_manufacturer, conn)


    # now we have that, we need to load the excel file
    fn = get_excel_file('ultrasound')
    df_ultrasound = pd.read_excel(fn)
    df_ultrasound = df_ultrasound.fillna()

    # LOAD MANUFACTURERS pandas series
    excel_manufacturers = set(df_ultrasound['Company'].str.upper())
    ap_manufacturers = set(df_manufacturer['MANUFACTURER'].str.upper())

    # check which ones already exist in database
    manufactuers_to_add = get_new_manufacturers(excel_manufacturers, ap_manufacturers)
    # update database with the new manufacturers
    if len(manufactuers_to_add) > 0:
        update_ap(sql_mapping.sql_man_insert, manufactuers_to_add, conn, cursor)

    # TODO load gmdn table

    # TODO load model table


def format_cell(cell):
    """
    Cell contents converted to string, remove ' and special chars
    Returns formatted string in uppercase
    """
    p = re.compile('(?![ -~]).')
    in_str = str(cell)
    in_str = in_str.replace("'","")
    in_str = p.sub('', in_str)
    return in_str.upper()

def get_ap_table(sql_query, db_conn):
    """
    Creates, fills and returns a dataframe with results from a SQL query to the database
    """
    data = pd.read_sql_query(sql_query, db_conn)
    df = pd.DataFrame(data)
    return df

def get_excel_file(name):
    """
    Chooses correct filename based on input string:
    pulse = pulse-oximeter dataset
    ultrasound = ultrasound dataset
    """
    if name == "pulse":
        fn = "C:\\Users\\212628255\\Documents\\GE\\AssetPlus\\7 Projects\\GMDN\\Pulse_result1.xlsx"
    elif name == "ultrasound":
        fn = "C:\\Users\\212628255\\Documents\\GE\\AssetPlus\\7 Projects\\GMDN\\Ultrasonic_GE_2020-06-04.xlsx"
    else:
        return 'No file associated'
    return fn

def get_new_manufacturers(new_source, ap_source):
    """
    Checks delta between two pandas series and returns only the records that are don't exist in the DB
    """
    new_records = set()
    existing = set()
    for new_man in new_source:
        new_man = new_man[:50]  # limited to 50 chars hence ensure we check like for like
        if new_man not in ap_source:
            print("Added NEW {}".format(new_man))
            new_records.add(new_man)
        else:
            print("IGNORE {}".format(new_man))
            existing.add(new_man)
    return new_records




def update_ap(sql_insert, records, connection, cursor):
    """
    Generic function to update a DB on a one-by-one basis
    :param sql_insert: Query string
    :param records: List of records
    :param connection: OBDC
    :param cursor: Iterator
    :return:
    """
    cnt = 0
    for record in records:
        print("Adding {}".format(record))
        cursor.execute("INSERT INTO MARQUES (MA_NOM) VALUES (?)", record)
        cnt += 1
    connection.commit()
    print("{} records inserted successfully".format(str(cnt)))


if __name__ == "__main__":
    main()
