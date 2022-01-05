
from pathlib import Path
import csv
from datetime import datetime, timedelta


dir = Path(r"C:\Users\212628255\Documents\2 GE\AssetPlus\7 Projects\Missing Next PM Dates")
output = Path(r"C:\Users\212628255\Documents\2 GE\AssetPlus\7 Projects\Missing Next PM Dates\output")
fn = "MISSING_PM_DATES.csv"

def update_last_pm_eq1996(asset, next):
    sql = f"-- {asset}\n" \
          f"UPDATE B_EQ1996 SET D_PRO_I_P = '{next}' WHERE N_IMMA = '{asset}'"
    return sql


def date_to_str(dt):
    return dt.strftime("%Y%m%d")


def str_to_date(date_string: str) -> datetime:
    """Helper function for converting string to date"""
    return datetime.strptime(date_string, '%d/%m/%Y').date()



header = ['N_IMMA','N_PRODUIT_FOUR','MES1','D_DER_I_P','D_PRO_I_P']

if __name__ == "__main__":
    with open(dir / fn, "r") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",", fieldnames=header)
        for row in reader:
            # print(row)
            asset = row['N_IMMA']
            produit = row['N_PRODUIT_FOUR']
            install = row['MES1']
            last = row['D_DER_I_P']
            next = row['D_PRO_I_P']
            if next == 'NULL':
                if not last == 'NULL':  # use last if exists
                    # convert last to a date
                    last_date = str_to_date(last)

                else:
                    last_date = str_to_date(install)

                next_date = last_date + timedelta(days=365)
                print(update_last_pm_eq1996(asset,date_to_str(next_date)))






