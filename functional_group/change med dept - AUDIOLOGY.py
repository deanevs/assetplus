

def main():

    for n in range(len(cx)):
        asset = cx[n][0]
        prev_code = cx[n][1]
        code_med = 'CX-AUDTBC'
        med_name = 'AUDIOLOGY CX TBC'

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

    for n in range(len(sm)):
        asset = sm[n][0]
        prev_code = sm[n][1]
        code_med = 'SM-AUDTBC'
        med_name = 'AUDIOLOGY SM TBC'

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


cx = [
('536892','SOAUD'),
('AP-21102','SOAUD'),
('AP-21101','SOAUD'),
('AP-22044','SOAUD'),
('AP-22046','SOAUD'),
('AP-22047','SOAUD'),
('536134','SOAUD'),
('539609','SOAUD'),
('512220','SOAUD'),
('512221','SOAUD'),
('514437','SOAUD'),
('514639','SOAUD'),
('516525','SOAUD'),
('527439','SOAUD')
]

sm = [
    ('543157','AUDSMH'),
('511708','AUDSMH'),
('AP-24517','AUDSMH'),
('536867','AUDSMH'),
('535107','PRU'),
('543367','PRU'),
('509576','PRU')
]

if __name__ == '__main__':
    main()