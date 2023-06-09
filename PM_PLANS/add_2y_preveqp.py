from pathlib import Path
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta


pd.options.display.max_columns = 20
pd.options.display.max_rows = 100
pd.options.display.width = 1000


workdir = Path(r'C:\Users\212628255\Documents\2 GE\AssetPlus\7 Projects\20230506 - 7Y PM PLAN FLOW')
filename = 'pm-7y-flow-DATES.csv'


def main():
    df = pd.read_csv(workdir / filename)
    print(df.head())

    for idx, row in df.iterrows():
        asset = row['N_IMMA']
        dt = row['DATE_PREV']
        new_date_str = update_next_pm(str(dt))
        print(f"UPDATE PREV_EQP SET DATE_PREV = '{new_date_str}' WHERE N_IMMA = '{asset}'")


def update(asset):
    return f"UPDATE PREV_EQP SET NU_PREVENT = '7Y-FLOW' WHERE N_IMMA = '{asset}'"


def update_next_pm(dt):
    # convert date
    prev_date = datetime.strptime(dt, "%Y%m%d")
    # add 2 years
    new_date = (prev_date + relativedelta(years=2)).date()
    new_date_str = datetime.strftime(new_date, "%Y%m%d")
    return new_date_str


if __name__ == '__main__':
    main()