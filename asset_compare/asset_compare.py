import pandas as pd

input_path = "C:\\Users\\212628255\\Documents\\GE\\AssetPlus\\7 Project Management\\New Database\\"
input_file1 = "B_EQ1996_ACTIVE.csv"     # from assetplus B_EQ1996
input_file2 = "SPIRE_BIOMED.xlsx"       # Lisa DB file that excludes DI assets (approx 500)

desired_width = 420
pd.set_option('display.width', desired_width)
pd.options.display.max_colwidth = 200
pd.set_option("display.precision", 4)
pd.set_option("display.expand_frame_repr", False)
pd.set_option("display.max_rows", None)
# pd.set_option("display.max_cols", None)

data_ap = pd.read_csv(input_path + input_file1, low_memory=False)
data_ge = pd.read_excel(input_path + input_file2)

print(data_ap.head())
print(data_ge.head())

# difference = data_ap[data_ap['N_IMMA'] != data_ge['Asset Number']]
# print(difference)

# print(data_ap.shape)
# print(data_ge.shape)

diff = data_ap.where(data_ap['N_IMMA'].values == data_ge['Asset Number'].values)
print(diff)