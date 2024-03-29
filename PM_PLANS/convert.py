from pathlib import Path
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta


pd.options.display.max_columns = 20
pd.options.display.max_rows = 100
pd.options.display.width = 1000


workdir = Path(r'C:\Users\212628255\Documents\2 GE\AssetPlus\7 Projects\20230506 - 7Y PM PLAN FLOW')
filename = 'flow meters 5 year.xlsx'
filename2 = 'pm-7y-flow-DATES'


def main():
    # df = pd.read_excel(workdir / filename)
    df = pd.read_csv(workdir / filename2)

    print(df.head())
    print(len(df))

    # df_flow = df[df.Name.str.contains('FLOW', case=False)]
    # print(f"New length with flow = {len(df_flow)}")

    for idx, row in df_flow.iterrows():
        asset = row['Asset No']
        name = row.Name
        print(update(asset))


def update(asset):
    return f"UPDATE PREV_EQP SET NU_PREVENT = '7Y-FLOW' WHERE N_IMMA = '{asset}'"

def update_next_pm(asset, dt):
    # convert date
    prev_date = datetime.strptime(dt, "%Y%m%d")
    # add 2 years
    new_date = prev_date + relativedelta(years=2)
    print(new_date)






if __name__ == '__main__':
    main()