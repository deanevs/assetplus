"""
Process:
1. Run the SQL on AP
2. Export the csv file to the 'dir' below
3. Run the program
4. Export and load the sql generated into AP
"""
from pathlib import Path
import csv
from datetime import datetime, timedelta
import sys


dir = Path(r"C:\Users\212628255\Documents\2 GE\AssetPlus\7 Projects\Missing Next PM Dates")
output = Path(r"C:\Users\212628255\Documents\2 GE\AssetPlus\7 Projects\Missing Next PM Dates\output")
fn = "SIEBEL START DATES FOR PM JOBS.csv"
sql = "next_pm_" + datetime.today().date().strftime("%Y-%m-%d") + ".sql"


def update_ft1996(asset, call, wo):

    return f"UPDATE B_FT1996 SET DA_AP = '{call}', DA_INT = '{call}' WHERE NU_IMM = '{asset}' AND NU_INT = '{wo}'"


def convert_date(dt):
    return dt[:4] + '-' + dt[4:6] + '-' + dt[6:]


header = ['NU_INT', 'N_IMMA','DA_AP','DA_INT', 'DA_FIN','debrief_start','debrief_end']

if __name__ == "__main__":

    with open(dir / fn, "r") as csvfile:
        with open(output / sql, 'w') as outfile:
            reader = csv.DictReader(csvfile, delimiter=",", fieldnames=header)
            first_row = True
            for row in reader:
                if first_row:
                    first_row = False
                    continue

                asset = row['N_IMMA'][1:]   # remove ' char
                debrief = row['debrief_start']
                wo = row['NU_INT']
                sqlout = update_ft1996(asset,convert_date(debrief), wo) + '\n'

                outfile.writelines(sqlout)
        outfile.close()
    csvfile.close()






