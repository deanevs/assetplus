import pandas as pd
import numpy as np
from collections import defaultdict


def main():
    fn = 'C:\\Users\\212628255\\Documents\\GE\AssetPlus\\7 Projects\\New Database\\SPIRE PYTHON TEMPLATE FILE.xlsx'

    # create dataframe
    df = pd.read_excel(fn, sheet_name='PREV_MAINT')

    retired = []
    current = []

    for index, row in df.iterrows():
        pm_no = str(row['PM No']).strip()
        pm_title = str(row['PM Title']).strip()

        if 'USE' in pm_title:
            retired.append((pm_no, pm_title))
        elif 'GEPP' in pm_no:
            continue
            # print(pm_no)
        else:
            current.append((pm_no, pm_title))
            site = pm_title.split('-')[0]
            device = pm_title.split('-')[1]
            print(site)
            if 'MVS' in device:
                mvs = device.split(' ')[0]
            #     device = device.split(' ')[1]
                print('\t' + mvs)
            #     print('\t' + device)
            # else:
            print('\t' + device)

    # print("RETIRED")
    # for r in retired:
    #     print(r[0],r[1])
    #
    # print("CURRENT")
    # for c in current:
    #     print(c[0], c[1])

if __name__ == '__main__':
    main()