import pandas as pd

FILE_MASTER = 'C:\\Users\\212628255\\Documents\\GE\\AssetPlus\\7 Projects\\New Database\\DB_GMDN.xlsx'

df = pd.read_excel(FILE_MASTER)

header = df[0]

print(header)

