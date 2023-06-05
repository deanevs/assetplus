from pathlib import Path
import pandas as pd


pd.options.display.max_columns = 20
pd.options.display.max_rows = 100
pd.options.display.width = 1000


workdir = Path(r'C:\Users\212628255\Documents\2 GE\AssetPlus\7 Projects\20230506 - 7Y PM PLAN FLOW')
filename = 'flow meters 5 year.xlsx'


def main():
    df = pd.read_excel(workdir / filename)
    print(df.head())
    print(len(df))

    df_flow = df[df.Name.str.contains('FLOW', case=False)]
    print(f"New length with flow = {len(df_flow)}")

    for idx, row in df_flow.iterrows():
        asset = row['Asset No']
        name = row.Name
        print(update(asset))


def update(asset):
    return f"UPDATE PREV_EQP SET NU_PREVENT = '7Y-FLOW' WHERE N_IMMA = '{asset}'"




if __name__ == '__main__':
    main()