import pandas as pd
from pathlib import Path
from fuzzywuzzy import fuzz

pd.set_option('max_columns', None)
pd.set_option("max_rows", None)
pd.set_option('display.width', 1000)

dir_path = Path(r"C:\Users\212628255\Documents\GE\AssetPlus\7 Projects\GMDN")
file_to_open1 = dir_path / "ap_gmdn.csv"
file_to_open2 = dir_path / "GMDN_TERMS.csv"     #"gmdn_code_terms.csv"

df_ap = pd.read_csv(file_to_open1)
df_gmdn = pd.read_csv(file_to_open2)


df_ap.drop(columns=['F_SPECC','F_SPECL','F_SPECL2','F_RET','EQ_AMT_COM','CRIT_AC','CRIT_ACT','NU_COMPTE','INSERT_DATE',
                    'UPDATE_DATE','RISKCODE','ECR_MODCODE','REMP_PRIX','CH1','CH2','CH3','CH4','CH5'], inplace=True)

print(df_ap.head())
print(df_gmdn.head())

headers = ['AP code', 'AP term', 'GMDN_CODE','TERM_NAME','simple', 'partial', 'token sort', 'token set']
df_results = pd.DataFrame(columns=headers)

no_rows = len(df_gmdn)

for index, row in df_ap.iterrows():     # outer loop - assetplus gmdn
    ap_gmdn_term = row['NOM']
    ap_gmdn_code = row['N_NOM_CNEH']

    # init holders to store max result for each inner loop
    max_code_term = tuple()
    max_result = tuple()
    max_holder = 0
    cnt = 0         # used to know its the last itteration

    for idx_gm, row_gm in df_gmdn.iterrows():   # inner loop - official gmdn
        gm_gmdn_term = row_gm['TERM_NAME']
        gm_gmdn_code = row_gm['GMDN_CODE']

        # the scorers are typically token since similar words in different order
        # sum all 4 ratios allows for different scenarios
        simple = fuzz.ratio(ap_gmdn_term, gm_gmdn_term)
        partial = fuzz.partial_ratio(ap_gmdn_term, gm_gmdn_term)
        token_sort = fuzz.token_sort_ratio(ap_gmdn_term, gm_gmdn_term)
        token_set = fuzz.token_set_ratio(ap_gmdn_term, gm_gmdn_term)

        sum = (simple + partial + token_sort + token_set)

        # store highest ratio
        if sum > max_holder:
            max_holder = sum
            max_code_term = (gm_gmdn_code, gm_gmdn_term)
            max_result = (simple, partial, token_sort, token_set)

        # last itteration save result
        cnt += 1
        if cnt == no_rows:
            print("{}\t{}".format(ap_gmdn_code, ap_gmdn_term))
            print(max_code_term)
            print(max_result)
            df_results = df_results.append({'AP code':ap_gmdn_code,
                               'AP term':ap_gmdn_term,
                               'GMDN_CODE':max_code_term[0],
                               'TERM_NAME':max_code_term[1],
                               'simple': max_result[0],
                               'partial':max_result[1],
                               'token sort':max_result[2],
                               'token set':max_result[3]
                               }, ignore_index=True)


df_results.to_excel("gmdn_result2.xlsx", index=False)




