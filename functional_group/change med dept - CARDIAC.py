

def main():

    for n in range(len(asset_list)):
        asset = asset_list[n][0]
        prev_code = asset_list[n][1]
        site = asset_list[n][2]
        if site == 'CX':
            code_med = 'CX-LUNTBC'
            med_name = 'LUNG FUNCTION CX TBC'
        elif site == 'HH':
            code_med = 'HH-CARTBC'
            med_name = 'CARDIAC HH TBC'
        elif site == 'SM':
            code_med = 'SM-LUNTBC'
            med_name = 'LUNG FUNCTION SM TBC'

        sql_start = f"IF EXISTS ( SELECT * FROM B_EQ1996 WHERE N_IMMA = '{asset}' AND DATE_REFOR IS NULL )" \
                    f"\nBEGIN" \
                    f""

        sql_update_b_eq1996 = f"UPDATE B_EQ1996 SET N_UF= '{code_med}',EX_N_UF= '{prev_code}' WHERE  N_IMMA = '{asset}'"
        sql_update_prev_eqp = f"UPDATE PREV_EQP SET N_UF = '{code_med}', NOM_UF = '{med_name}'" \
                              f"WHERE  (PREV_EQP.GENERIC IS NULL OR GENERIC=0) AND N_IMMA IS NOT NULL AND PREV_EQP.N_IMMA='{asset}'"

        print(sql_start)
        print(sql_update_b_eq1996)
        print(sql_update_prev_eqp)
        print('END;')
        print('GO')


asset_list = [
('103071','90','HH'),
('533400','90','HH')
]

if __name__ == '__main__':
    main()