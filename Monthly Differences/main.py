"""
1. Get todays date
2. Set it to the 1st day of month
3. Use timedelta and subtract 1 day

"""

import datetime
import pandas as pd
from pathlib import Path
import sys

pd.set_option('max_columns', None)  # displays all columns
pd.set_option("max_rows", None)     # displays all rows ... change None to 100 ow whatever number
pd.set_option('display.width', 1000)

wdire = Path(r'C:\Users\212628255\Documents\2 GE\AssetPlus\7 Projects\20220822 - Added Retired Monthly Differences')
df = pd.read_csv((wdire / 'monthly-pm-status.csv'))
df['collected'] = pd.to_datetime(df['collected']).dt.date

today = datetime.date.today()
this_month_first = today.replace(day=1)
end_last_month = this_month_first - datetime.timedelta(days=1)
print(end_last_month)

last_month_first = end_last_month.replace(day=1)
end_month_before_last = last_month_first - datetime.timedelta(days=1)
print(end_month_before_last)

df_last = df.loc[df.collected == pd.Timestamp(end_last_month)]
df_lastlast = df.loc[df.collected == pd.Timestamp(end_month_before_last)]

print(df_last.head())
print(df_lastlast.head())

merged = pd.merge(df_last,df_lastlast,how='outer',on='n_imma')
# print(merged)

added = merged[merged['collected_y'].isna()]
print(added.tech_dept_x.value_counts())

retired = merged[merged['collected_x'].isna()]
print(retired.tech_dept_y.value_counts())

import matplotlib as plt
retired.tech_dept_y.value_counts().plot(kind='bar')


# df.sort_values(ascending=False, inplace=True, by=['collected','n_imma'], ignore_index=True)
# print(df)
#
# grp = df.groupby('collected')
# # print(grp.groups.keys())
# print([x for x in grp.groups.keys()])



# if __name__ == '__main__':
#     main()