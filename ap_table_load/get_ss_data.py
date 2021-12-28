import smartsheet
import pandas as pd
import gc



ACCESS_TOKEN = '2s72jhlhz5470vo0culgpusmf4'
USER_SH_ID = 2653924667746180

# def get_cell_value(row, column_name):
#     """Returns cell value from the row and column name"""
#     cell = row.get_column(column_map[column_name])
#     return cell.value


def map_columns(sh):
    dict = {}
    for col in sh.columns:
        dict[col.title] = col.id
    return dict




def main():
    ss_client = smartsheet.Smartsheet(ACCESS_TOKEN)
    user_sh = ss_client.Sheets.get_sheet(USER_SH_ID, page_size=1000)

    # map columns
    user_col_map = map_columns(user_sh)

    for k,v in user_col_map.items():
        print(k,v)



if __name__ == "__main__":
    main()
