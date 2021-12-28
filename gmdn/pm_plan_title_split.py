import pandas as pd
import numpy as np
from collections import defaultdict


def main():
    fn = 'C:\\Users\\212628255\\Documents\\GE\AssetPlus\\7 Projects\\New Database\\SPIRE PYTHON TEMPLATE FILE.xlsx'

    # create dataframe
    df = pd.read_excel(fn, sheet_name='PREV_MAINT')

    d = defaultdict(list)

    count = 0
    count_OL = 0
    cnt_single = 0

    not_used = []

    for index, row in df.iterrows():
        # print("***************")
        pm_no = str(row['PM No']).strip()
        pm_title = str(row['PM Title']).strip()
        hospital = pm_title.split('-')[0].strip()

        if 'NOT IN USE' in pm_title:
           not_used.append(pm_no)

        if 'GEPPM' in pm_no:
            count += 1
        else:
            count_OL += 1
            try:
                if 'MVS' in pm_title.split('-')[1]:
                    temp = pm_title.split('-')[1].split(' ', maxsplit=1)
                    mvs = temp[0].strip()
                    device = temp[1]
                    use = ''
                    if '(' in device:
                        temp = device[device.find("(")+1:device.find(")")]
                        if 'OL' in temp.split(' ')[1] and temp.split(' ')[1] != 'ISOLATION':
                             use = temp.split(' ')[1]
                    if use != '':
                        d[use].append(pm_no)
                        # print(pm_no)
                        # print(hospital)
                        # print(mvs)
                        # print(device)
                        # print(use)
                else:
                    cnt_single += 1
                    # print(pm_no + '\t' + pm_title)
            except:
                continue
                # print("EXCEPT:  " + pm_no + '\t' + pm_title)

    no_values = 0
    for k, v in d.items():
        no_values += len(v)
        print("KEEP =>\t{}\t\t\tRETIRE =>\t{}".format(k,v))

    print("Number of GEPPM = {}".format(str(count)))
    print("Number of OL = {}".format(str(count_OL)))
    print("Number of OL PMs after consolidate = {}".format(str(len(d.keys()))))
    print("Number of PMs to consolidate = {}".format(str(no_values)))


    # print(not_used)
    # print("Messed up PM Plans = {}".format(str(count)))

    # print("RETIRED")
    # for r in retired:
    #     print(r[0],r[1])
    #
    # print("CURRENT")
    # for c in current:
    #     print(c[0], c[1])

if __name__ == '__main__':
    main()