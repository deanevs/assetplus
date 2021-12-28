

def main():
    asset = ''
    code_med = ''
    # code_med_cx = 'CX-AUDTBC'
    # code_med_sm = 'SM-AUDTBC'

    prev_code = ''
    # for n in range(len(cx)):
    #     asset = cx[n][0]
    #     prev_code = cx[n][1]
    #     code_med = 'CX-AUDTBC'
    #     med_name = 'AUDIOLOGY CX TBC'
    #
    #     sql_update_b_eq1996 = f"UPDATE B_EQ1996 SET N_UF= '{code_med}',EX_N_UF= '{prev_code}' WHERE  N_IMMA = '{asset}'"
    #     sql_update_prev_eqp = f"UPDATE PREV_EQP SET N_UF = '{code_med}', NOM_UF = '{med_name}'" \
    #                           f"WHERE  (PREV_EQP.GENERIC IS NULL OR GENERIC=0) AND N_IMMA IS NOT NULL AND PREV_EQP.N_IMMA='{asset}'"
    #
    #     print(sql_update_b_eq1996)
    #     print(sql_update_prev_eqp)
    #     print('GO')

    for n in range(len(sm)):
        asset = sm[n][0]
        prev_code = sm[n][1]
        code_med = 'SM-VASTBC'
        med_name = 'VASCULAR SM TBC'

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


sm = [
('528227','IRVAS'),
('AP-17674','IRVAS'),
('AP-18645','IRVAS')
]


if __name__ == '__main__':
    main()