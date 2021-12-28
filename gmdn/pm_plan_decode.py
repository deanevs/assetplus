import pandas as pd
import numpy as np
from collections import defaultdict


def main():
    fn = 'C:\\Users\\212628255\\Documents\\Copy of GE-MVS Spire 31-Aug-20 OKM MVS.AH.xlsx'

    # create dataframe
    df = pd.read_excel(fn, sheet_name='Asset List')

    # init data structure to hold
    # dic[ 'MVS001' : ' Deive description']
    dict = {}

    for index, row in df.iterrows():
        code = str(row['code']).strip()
        desc = str(row['description']).strip()

        if code in dict.keys():
            continue
        else:
            dict[code] = desc


    for k,v in dict.items():
        print(k,v)

if __name__ == '__main__':
    main()