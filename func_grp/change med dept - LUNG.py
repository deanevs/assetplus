

def main():

    for n in range(len(asset_list)):
        asset = asset_list[n][0]
        prev_code = asset_list[n][1]
        site = asset_list[n][2]
        if site == 'CX':
            code_med = 'CX-LUNTBC'
            med_name = 'LUNG FUNCTION CX TBC'
        elif site == 'HH':
            code_med = 'HH-LUNTBC'
            med_name = 'LUNG FUNCTION HH TBC'
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
('516533','NOLUN','CX'),
('532013','LUFUN','HH'),
('532014','LUFUN','HH'),
('532015','LUFUN','HH'),
('532016','LUFUN','HH'),
('532020','LUFUN','HH'),
('532021','LUFUN','HH'),
('532023','LUFUN','HH'),
('532024','LUFUN','HH'),
('532025','LUFUN','HH'),
('532054','LUFUN','HH'),
('532132','LUFUN','HH'),
('57013','LUFUN','HH'),
('534841','LUFUN','HH'),
('534842','LUFUN','HH'),
('534843','LUFUN','HH'),
('503199','LUFUN','HH'),
('503200','LUFUN','HH'),
('AP-19188','LUFUN','HH'),
('520998','LUFUN','HH'),
('521000','LUFUN','HH'),
('521595','LUFUN','HH'),
('523491','LUFUN','HH'),
('104926','COMMCARDRESP','SM'),
('AP-17935','LUNG-SMH','SM'),
('535003','LUNG-SMH','SM'),
('AP-17943','LUNG-SMH','SM'),
('AP-17944','LUNG-SMH','SM'),
('306957','LUNG-SMH','SM'),
('302990','LUNG-SMH','SM'),
('306505','LUNG-SMH','SM'),
('AP-24913','LUNG-SMH','SM'),
('AP-23405','LUNG-SMH','SM'),
('303012','LUNG-SMH','SM'),
('304597','LUNG-SMH','SM'),
('TEQ60','LUNG-SMH','SM'),
('518353','LUNG-SMH','SM'),
('519763','LUNG-SMH','SM'),
('519764','LUNG-SMH','SM'),
('519765','LUNG-SMH','SM'),
('519766','LUNG-SMH','SM'),
('519767','LUNG-SMH','SM'),
('519768','LUNG-SMH','SM'),
('519769','LUNG-SMH','SM'),
('519770','LUNG-SMH','SM'),
('519771','LUNG-SMH','SM'),
('528176','LUNG-SMH','SM'),
('528177','LUNG-SMH','SM'),
('528178','LUNG-SMH','SM'),
('528236','LUNG-SMH','SM'),
('528618','LUNG-SMH','SM'),
('528620','LUNG-SMH','SM'),
('308157','LUNG-SMH','SM'),
('528987','LUNG-SMH','SM'),
('19874','LUNG-SMH','SM'),
('19488','LUNG-SMH','SM'),
('19487','LUNG-SMH','SM'),
('19485','LUNG-SMH','SM'),
('18987','LUNG-SMH','SM'),
('18255','LUNG-SMH','SM'),
('17851','LUNG-SMH','SM'),
('17552','LUNG-SMH','SM'),
('17505','LUNG-SMH','SM'),
('100759','LUNG-SMH','SM'),
('537288','LUNG-SMH','SM'),
('18438','LUNG-SMH','SM'),
('AP-17157','LUNG-SMH','SM'),
('303583','LUNG-SMH','SM'),
('305346','LUNG-SMH','SM'),
('304231','LUNG-SMH','SM'),
('543105','LUNG-SMH','SM'),
('543106','LUNG-SMH','SM'),
('543347','LUNG-SMH','SM'),
('543348','LUNG-SMH','SM'),
('543349','LUNG-SMH','SM'),
('543469','LUNG-SMH','SM'),
('543470','LUNG-SMH','SM'),
('543725','LUNG-SMH','SM'),
('543736','LUNG-SMH','SM'),
('306956','LUNG-SMH','SM'),
('303290','LUNG-SMH','SM'),
('303289','LUNG-SMH','SM'),
('303169','LUNG-SMH','SM'),
('303168','LUNG-SMH','SM'),
('303165','LUNG-SMH','SM'),
('303164','LUNG-SMH','SM'),
('303163','LUNG-SMH','SM'),
('303162','LUNG-SMH','SM'),
('303159','LUNG-SMH','SM'),
('303158','LUNG-SMH','SM'),
('303157','LUNG-SMH','SM'),
('303155','LUNG-SMH','SM'),
('303121','LUNG-SMH','SM'),
('303111','LUNG-SMH','SM'),
('303096','LUNG-SMH','SM'),
('303095','LUNG-SMH','SM'),
('303093','LUNG-SMH','SM'),
('303092','LUNG-SMH','SM'),
('302999','LUNG-SMH','SM'),
('302987','LUNG-SMH','SM'),
('302290','LUNG-SMH','SM'),
('302289','LUNG-SMH','SM'),
('302285','LUNG-SMH','SM'),
('302284','LUNG-SMH','SM'),
('302200','LUNG-SMH','SM'),
('302164','LUNG-SMH','SM'),
('302039','LUNG-SMH','SM'),
('301783','LUNG-SMH','SM'),
('301598','LUNG-SMH','SM'),
('300841','LUNG-SMH','SM'),
('300712','LUNG-SMH','SM'),
('300617','LUNG-SMH','SM'),
('300107','LUNG-SMH','SM'),
('15979','LUNG-SMH','SM'),
('15852','LUNG-SMH','SM'),
('304379','LUNG-SMH','SM'),
('304380','LUNG-SMH','SM'),
('304381','LUNG-SMH','SM'),
('304382','LUNG-SMH','SM'),
('304488','LUNG-SMH','SM'),
('304586','LUNG-SMH','SM'),
('304587','LUNG-SMH','SM'),
('304588','LUNG-SMH','SM'),
('304594','LUNG-SMH','SM'),
('304647','LUNG-SMH','SM'),
('304690','LUNG-SMH','SM'),
('304691','LUNG-SMH','SM'),
('304692','LUNG-SMH','SM'),
('304718','LUNG-SMH','SM'),
('304826','LUNG-SMH','SM'),
('304827','LUNG-SMH','SM'),
('305008','LUNG-SMH','SM'),
('305009','LUNG-SMH','SM'),
('306060','LUNG-SMH','SM'),
('306572','LUNG-SMH','SM'),
('306773','LUNG-SMH','SM'),
('306951','LUNG-SMH','SM'),
('306952','LUNG-SMH','SM'),
('306953','LUNG-SMH','SM'),
('306954','LUNG-SMH','SM'),
('306994','LUNG-SMH','SM'),
('307257','LUNG-SMH','SM'),
('307258','LUNG-SMH','SM'),
('307259','LUNG-SMH','SM'),
('307260','LUNG-SMH','SM'),
('307261','LUNG-SMH','SM'),
('307262','LUNG-SMH','SM'),
('307370','LUNG-SMH','SM'),
('307371','LUNG-SMH','SM'),
('307372','LUNG-SMH','SM'),
('307373','LUNG-SMH','SM'),
('307374','LUNG-SMH','SM'),
('307971','LUNG-SMH','SM'),
('307972','LUNG-SMH','SM'),
('307973','LUNG-SMH','SM'),
('308158','LUNG-SMH','SM'),
('308159','LUNG-SMH','SM'),
('308202','LUNG-SMH','SM'),
('308203','LUNG-SMH','SM'),
('304108','LUNG-SMH','SM'),
('304109','LUNG-SMH','SM'),
('304135','LUNG-SMH','SM'),
('304136','LUNG-SMH','SM'),
('304137','LUNG-SMH','SM'),
('304138','LUNG-SMH','SM'),
('304139','LUNG-SMH','SM'),
('304232','LUNG-SMH','SM'),
('304233','LUNG-SMH','SM'),
('304234','LUNG-SMH','SM'),
('304235','LUNG-SMH','SM'),
('304276','LUNG-SMH','SM'),
('304277','LUNG-SMH','SM'),
('304278','LUNG-SMH','SM'),
('304279','LUNG-SMH','SM'),
('304280','LUNG-SMH','SM'),
('304107','LUNG-SMH','SM'),
('304106','LUNG-SMH','SM'),
('304104','LUNG-SMH','SM'),
('304064','LUNG-SMH','SM'),
('304063','LUNG-SMH','SM'),
('304030','LUNG-SMH','SM'),
('303956','LUNG-SMH','SM'),
('303955','LUNG-SMH','SM'),
('303954','LUNG-SMH','SM'),
('303952','LUNG-SMH','SM'),
('303950','LUNG-SMH','SM'),
('303906','LUNG-SMH','SM'),
('303905','LUNG-SMH','SM'),
('303904','LUNG-SMH','SM'),
('303903','LUNG-SMH','SM'),
('303781','LUNG-SMH','SM'),
('303777','LUNG-SMH','SM'),
('303559','LUNG-SMH','SM'),
('303539','LUNG-SMH','SM'),
('303537','LUNG-SMH','SM'),
('303534','LUNG-SMH','SM'),
('303531','LUNG-SMH','SM'),
('303492','LUNG-SMH','SM'),
('303491','LUNG-SMH','SM'),
('303490','LUNG-SMH','SM'),
('303489','LUNG-SMH','SM'),
('303488','LUNG-SMH','SM'),
('303487','LUNG-SMH','SM'),
('303486','LUNG-SMH','SM'),
('303485','LUNG-SMH','SM'),
('303484','LUNG-SMH','SM'),
('303483','LUNG-SMH','SM'),
('303482','LUNG-SMH','SM'),
('303481','LUNG-SMH','SM'),
('303480','LUNG-SMH','SM'),
('303479','LUNG-SMH','SM'),
('303478','LUNG-SMH','SM'),
('303477','LUNG-SMH','SM'),
('303476','LUNG-SMH','SM'),
('303475','LUNG-SMH','SM'),
('303419','LUNG-SMH','SM'),
('303352','LUNG-SMH','SM'),
('303348','LUNG-SMH','SM'),
('303347','LUNG-SMH','SM'),
('303346','LUNG-SMH','SM'),
('303292','LUNG-SMH','SM'),
('303291','LUNG-SMH','SM'),
('506611','LUNG-SMH','SM'),
('506612','LUNG-SMH','SM'),
('509490','LUNG-SMH','SM'),
('509509','LUNG-SMH','SM'),
('509510','LUNG-SMH','SM'),
('509537','LUNG-SMH','SM'),
('511167','LUNG-SMH','SM'),
('511168','LUNG-SMH','SM'),
('511169','LUNG-SMH','SM'),
('511244','LUNG-SMH','SM'),
('511245','LUNG-SMH','SM'),
('511246','LUNG-SMH','SM'),
('511322','LUNG-SMH','SM'),
('511323','LUNG-SMH','SM'),
('511324','LUNG-SMH','SM'),
('511325','LUNG-SMH','SM'),
('511326','LUNG-SMH','SM')
]

if __name__ == '__main__':
    main()