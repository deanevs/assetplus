"""
Changes from one contract to another
Steps:
- run a single update in AP and collect query from WHO_DO_WHAT
- Copy and paste the queries into below sql
- substitute the string parameters within the query as below
1. Update B_EQ1996 with new contract number
2. Insert into HIST_EQ the asset and new contract
3. Delete from HIST_EQ the asset and old contract
"""

def main():
    new_contract = 'MMS PM ONLY 20-25'
    old_contract = 'TRUST - PCA PUMPS'

    for n_imma in asset_list_contract3:
        print(sql_update(old_contract, new_contract, n_imma))
        print(sql_insert(old_contract, new_contract, n_imma))
        print(sql_delete(old_contract, new_contract, n_imma))
        print('GO')


asset_list = ['504175',
'506184',
'507291',
'507381',
'200533',
'508897',
'543080',
'504739',
'513580',
'509573',
'517394',
'518954',
'306396',
'521882',
'521883',
'521930',
'522835',
'522930',
'525784',
'526367',
'500281',
'530132',
'500441',
'530484',
'530671',
'531399',
'531400',
'531401',
'531811',
'531818'
]


def sql_update(old_contract, new_contract, n_imma):
    return "UPDATE B_EQ1996 SET N_MARCHE = '{}', VAC_HT =  NULL, FRE_MP =  NULL, PD_MP =  NULL, NB_VCM =  NULL, DMCD_B = 0, PD_MC =  NULL, PD_SEUIL =0, " \
      "NB_AR_BL =  NULL, DMI = 0, T_IM =  NULL, NB_VCQ =  NULL, PD_MC_INT =0, PD_MP_INT = 0, P_M_PRIX_N = 0, P_M_TEMPOR = 1 WHERE N_IMMA = '{}'".format(new_contract, n_imma)

def sql_insert(old_contract, new_contract, n_imma):
    return "INSERT INTO HISTO_EQ (N_CONTRAT,CODE_TYPE,N_IMMA,ANNEE_EXO,DATE_EFFET,DATE_ECHU,PRORATA,TTC_ANNEE,HT_NET,TTC_NET,TTC_PREV,TTC_CORR,VAC_HT,FRE_MP,NB_VCM," \
             "PD_MP,PD_MC,PD_SEUIL,NB_AR_BL,DMCD_B,DMI,T_MI,DEFAUT,COMMENTAIRE,PARA1,GENERIC,GENERIC_SEQ,FK_LIEU_N_LIEU,FK_UNITES_N_UF,FK_BUDGET_NU_COMPTE,FK_BUDGET_AN_EXO," \
             "FINANCIAL_PERIOD_FROM,FINANCIAL_PERIOD_TO,INACTIVE_CONTRACT_ASSET_DATE,NB_VCQ,PD_MP_INT,PD_MC_INT,ASSET_ANNUAL_COST,ASSET_ANNUAL_NET_COST,YEAR_PERIOD_FROM," \
             "YEAR_PERIOD_TO,TAXE_CODE,TAXE_RATE,ASSET_ANNUAL_PRICE_HT,ASSET_ANNUAL_PRICE_TTC,ASSET_ANNUAL_PRICE_NET,ASSET_ANNUAL_COST_HT,ASSET_ANNUAL_COST_TTC," \
             "ASSET_ANNUAL_COST_NET,PREVIOUS_TAXE_RATE,PREVIOUS_DISCOUNT_RATE,PREVIOUS_PRORATA,CURRENT_PRORATA,PREV_ASSET_ANNUAL_PRICE_HT,PREV_ASSET_ANNUAL_COST_HT," \
             "IS_FIXE_PRICE_COST_USED) VALUES ('{}','COMP','{}',2021,'20210331','20220330',1,0,0,0,1,0,NULL,NULL,NULL,NULL,NULL,0,NULL,0,0,NULL,'2',NULL," \
             "'20210604','0',0,'SNEPIU','SONE2',NULL,NULL,'20210331','20220330',NULL,NULL,0,0,0,0,'20210331','20220330',NULL,0,0,0,0,0,0,0,0,0,0,0,0,0,0)".format(new_contract, n_imma)


def sql_delete(old_contract, new_contract, n_imma):
    return "DELETE HISTO_EQ  WHERE N_CONTRAT='{}' AND N_IMMA = '{}' AND FINANCIAL_PERIOD_FROM = '20210101'".format(old_contract, n_imma)

asset_list_contract3 = [
'533230',
'533231',
'533358',
'533359',
'533362',
'533363',
'533571',
'534015',
'534031',
'534033',
'534071',
'534384',
'534385',
'534386',
'534532',
'534534',
'534535',
'534536',
'534541',
'534542',
'534558',
'534559',
'534560',
'534561',
'534563',
'534564',
'534576',
'534578',
'534579',
'534580',
'534581',
'534582',
'534611',
'534612',
'534617',
'534625',
'534626',
'534649',
'534650',
'534656',
'534670',
'534696',
'534823',
'534825',
'534835',
'535362',
'535364',
'535367',
'535687',
'536076',
'536079',
'536107',
'536175',
'536176',
'536178',
'536407',
'536505',
'536647',
'536730',
'534618',
'534620',
'538028',
'538029',
'538080',
'538226',
'538354',
'538357',
'538359',
'538375',
'538437',
'202946',
'202949',
'202976',
'202981',
'202982',
'203131',
'539165',
'539212',
'539215',
'539225',
'539400',
'539446',
'539487',
'539796',
'539906',
'552058',
'552099',
'539393',
'520419',
'520420',
'520422',
'520423',
'520424',
'520425',
'520426',
'520428',
'520430',
'524195',
'527145',
'534814',
'535486',
'536074',
'536075',
'536562',
'539227']


# change from FULLY COMP to PM ONLY
asset_list_contract1 = [
'16624',
'504196',
'504295',
'17254',
'504376',
'504388',
'504393',
'504409',
'504533',
'504543',
'504568',
'504593',
'504763',
'505122',
'534827',
'534879',
'505450',
'505466',
'505467',
'505468',
'505547',
'505796',
'505801',
'505984',
'506073',
'506074',
'506076',
'506149',
'506328',
'506358',
'506411',
'506415',
'506447',
'535437',
'18429',
'18653',
'506532',
'507026',
'507030',
'507087',
'507088',
'507107',
'507113',
'507121',
'507128',
'507200',
'507202',
'507204',
'507206',
'507207',
'507209',
'507210',
'507211',
'507249',
'507309',
'19979',
'507552',
'507745',
'507795',
'507829',
'508269',
'508296',
'508298',
'508300',
'508301',
'508303',
'508305',
'508306',
'508307',
'508309',
'508313',
'508315',
'508363',
'508374',
'508383',
'508384',
'508387',
'508391',
'508409',
'508410',
'508414',
'508424',
'508425',
'508426',
'508428',
'508430',
'508431',
'508432',
'508449',
'508450',
'508506',
'508507',
'508516',
'508543',
'508549',
'508551',
'508573',
'508578',
'508580',
'508581',
'508614',
'508618',
'508620',
'508621',
'508648',
'508654',
'508688',
'508715',
'508733',
'202630',
'508803',
'508804',
'508880',
'508890',
'509133',
'509235',
'509336',
'202930',
'509495',
'509532',
'509551',
'509688',
'509790',
'539264',
'509820',
'509852',
'510110',
'510207',
'540020',
'540021',
'540125',
'540269',
'540591',
'510238',
'510254',
'510261',
'510320',
'510379',
'510383',
'510510',
'510525',
'510533',
'510612',
'510620',
'510681',
'541171',
'541173',
'517207',
'543266',
'543310',
'543601',
'543622',
'549020',
'549021',
'552038',
'501969',
'501971',
'502030',
'506009',
'508509',
'506734',
'507446',
'508310',
'508311',
'508411',
'508538',
'508539',
'508542',
'508874',
'513600',
'513849',
'513902',
'513912',
'513932',
'514177',
'514202',
'514210',
'514249',
'514252',
'514267',
'514459',
'514479',
'514780',
'514788',
'514790',
'514793',
'514795',
'514799',
'514867',
'514876',
'514903',
'514909',
'514911',
'514963',
'510690',
'515258',
'515261',
'515270',
'515398',
'515597',
'515607',
'515611',
'516128',
'516129',
'516130',
'516134',
'516138',
'516160',
'516173',
'516516',
'516657',
'516676',
'516683',
'516685',
'516718',
'516816',
'516823',
'516845',
'516858',
'516863',
'516904',
'517092',
'517156',
'517206',
'517224',
'517232',
'517291',
'517297',
'517300',
'517339',
'517354',
'517359',
'517409',
'517447',
'517739',
'517852',
'517967',
'518017',
'518106',
'518380',
'518386',
'518387',
'518417',
'518418',
'518669',
'518761',
'518763',
'304865',
'518882',
'518926',
'518993',
'305763',
'519101',
'519102',
'519189',
'519272',
'519292',
'519492',
'519678',
'306542',
'306960',
'520003',
'520015',
'520031',
'520047',
'520057',
'520086',
'520159',
'520163',
'520264',
'520331',
'308299',
'308301',
'308303',
'520563',
'520565',
'516669',
'516675',
'520671',
'520917',
'521027',
'521493',
'521523',
'521524',
'521525',
'521577',
'521949',
'521950',
'521951',
'521952',
'521953',
'521964',
'521978',
'522010',
'522012',
'522030',
'522044',
'522048',
'522069',
'522081',
'522095',
'522121',
'522136',
'103002',
'522165',
'522195',
'522203',
'522207',
'522233',
'522258',
'522294',
'522331',
'522351',
'522352',
'522355',
'522356',
'522357',
'522360',
'522364',
'522382',
'522567',
'522789',
'522790',
'522801',
'522813',
'522838',
'522852',
'522898',
'522901',
'522905',
'522907',
'522908',
'522911',
'522912',
'522914',
'522916',
'522918',
'522921',
'522935',
'522943',
'522965',
'522978',
'523000',
'523088',
'523089',
'523120',
'523135',
'523177',
'523247',
'523249',
'523402',
'105777',
'525129',
'525257',
'525268',
'525280',
'525318',
'525360',
'525362',
'525363',
'525364',
'525371',
'106540',
'525537',
'525539',
'525617',
'525690',
'525727',
'525728',
'525765',
'525766',
'525776',
'525777',
'525782',
'525802',
'525803',
'525827',
'520204',
'522527',
'525877',
'525887',
'525903',
'525915',
'525916',
'525918',
'525919',
'525982',
'526347',
'526349',
'526350',
'526584',
'527043',
'527045',
'527361',
'527433',
'527436',
'527466',
'527467',
'527474',
'527510',
'527513',
'527561',
'527665',
'528002',
'528003',
'528015',
'528018',
'528065',
'528066',
'528078',
'528080',
'528097',
'528168',
'528169',
'528195',
'528290',
'12356',
'12357',
'528315',
'528317',
'528320',
'528440',
'528492',
'528585',
'528593',
'528594',
'530997',
'528628',
'528697',
'529105',
'529106',
'529107',
'500227',
'500276',
'500284',
'500286',
'500293',
'529517',
'529545',
'530110',
'500384',
'500442',
'500449',
'500485',
'500527',
'500541',
'500580',
'500618',
'500651',
'500652',
'500699',
'530155',
'530162',
'530288',
'530343',
'530355',
'530391',
'530393',
'500772',
'500773',
'500834',
'500877',
'500901',
'500912',
'500957',
'500973',
'501037',
'501038',
'530672',
'530673',
'530675',
'530689',
'530692',
'530746',
'530995',
'530996',
'14957',
'501157',
'501189',
'501309',
'501339',
'501362',
'501382',
'501424',
'528627',
'531249',
'531258',
'531370',
'531374',
'531377',
'531383',
'531397',
'531407',
'531413',
'531446',
'531483',
'531499',
'501510',
'501607',
'501609',
'501678',
'501689',
'501699',
'501788',
'501812',
'502009',
'502017',
'502024',
'502052',
'502072',
'502076',
'502081',
'502094',
'502095',
'502123',
'502128',
'502130',
'502135',
'502149',
'502182',
'502193',
'502223',
'502224',
'502230',
'502241',
'531633',
'531705',
'531749',
'531839',
'531840',
'503051',
'503054',
'503055',
'503056',
'503057',
'503064',
'LSM116',
'531981',
'531982',
'531983',
'531985',
'532009',
'503178',
'503256',
'503265',
'503266',
'526364',
'530988',
'527120',
'500352',
'530198',
'530336',
'530337',
'530481',
'530737',
'531371',
'531372',
'531373',
'531463',
'540039',
'506023',
'16624',
'504196',
'504295',
'17254',
'504376',
'504388',
'504393',
'504409',
'504533',
'504543',
'504568',
'504593',
'504763',
'505122',
'534827',
'534879',
'505450',
'505466',
'505467',
'505468',
'505547',
'505796',
'505801',
'505984',
'506073',
'506074',
'506076',
'506149',
'506328',
'506358',
'506411',
'506415',
'506447',
'535437',
'18429',
'18653',
'506532',
'507026',
'507030',
'507087',
'507088',
'507107',
'507113',
'507121',
'507128',
'507200',
'507202',
'507204',
'507206',
'507207',
'507209',
'507210',
'507211',
'507249',
'507309',
'19979',
'507552',
'507745',
'507795',
'507829',
'508269',
'508296',
'508298',
'508300',
'508301',
'508303',
'508305',
'508306',
'508307',
'508309',
'508313',
'508315',
'508363',
'508374',
'508383',
'508384',
'508387',
'508391',
'508409',
'508410',
'508414',
'508424',
'508425',
'508426',
'508428',
'508430',
'508431',
'508432',
'508449',
'508450',
'508506',
'508507',
'508516',
'508543',
'508549',
'508551',
'508573',
'508578',
'508580',
'508581',
'508614',
'508618',
'508620',
'508621',
'508648',
'508654',
'508688',
'508715',
'508733',
'202630',
'508803',
'508804',
'508880',
'508890',
'509133',
'509235',
'509336',
'202930',
'509495',
'509532',
'509551',
'509688',
'509790',
'539264',
'509820',
'509852',
'510110',
'510207',
'540020',
'540021',
'540125',
'540269',
'540591',
'510238',
'510254',
'510261',
'510320',
'510379',
'510383',
'510510',
'510525',
'510533',
'510612',
'510620',
'510681',
'541171',
'541173',
'517207',
'543266',
'543310',
'543601',
'543622',
'549020',
'549021',
'552038',
'501969',
'501971',
'502030',
'506009',
'508509',
'506734',
'507446',
'508310',
'508311',
'508411',
'508538',
'508539',
'508542',
'508874',
'513600',
'513849',
'513902',
'513912',
'513932',
'514177',
'514202',
'514210',
'514249',
'514252',
'514267',
'514459',
'514479',
'514780',
'514788',
'514790',
'514793',
'514795',
'514799',
'514867',
'514876',
'514903',
'514909',
'514911',
'514963',
'510690',
'515258',
'515261',
'515270',
'515398',
'515597',
'515607',
'515611',
'516128',
'516129',
'516130',
'516134',
'516138',
'516160',
'516173',
'516516',
'516657',
'516676',
'516683',
'516685',
'516718',
'516816',
'516823',
'516845',
'516858',
'516863',
'516904',
'517092',
'517156',
'517206',
'517224',
'517232',
'517291',
'517297',
'517300',
'517339',
'517354',
'517359',
'517409',
'517447',
'517739',
'517852',
'517967',
'518017',
'518106',
'518380',
'518386',
'518387',
'518417',
'518418',
'518669',
'518761',
'518763',
'304865',
'518882',
'518926',
'518993',
'305763',
'519101',
'519102',
'519189',
'519272',
'519292',
'519492',
'519678',
'306542',
'306960',
'520003',
'520015',
'520031',
'520047',
'520057',
'520086',
'520159',
'520163',
'520264',
'520331',
'308299',
'308301',
'308303',
'520563',
'520565',
'516669',
'516675',
'520671',
'520917',
'521027',
'521493',
'521523',
'521524',
'521525',
'521577',
'521949',
'521950',
'521951',
'521952',
'521953',
'521964',
'521978',
'522010',
'522012',
'522030',
'522044',
'522048',
'522069',
'522081',
'522095',
'522121',
'522136',
'103002',
'522165',
'522195',
'522203',
'522207',
'522233',
'522258',
'522294',
'522331',
'522351',
'522352',
'522355',
'522356',
'522357',
'522360',
'522364',
'522382',
'522567',
'522789',
'522790',
'522801',
'522813',
'522838',
'522852',
'522898',
'522901',
'522905',
'522907',
'522908',
'522911',
'522912',
'522914',
'522916',
'522918',
'522921',
'522935',
'522943',
'522965',
'522978',
'523000',
'523088',
'523089',
'523120',
'523135',
'523177',
'523247',
'523249',
'523402',
'105777',
'525129',
'525257',
'525268',
'525280',
'525318',
'525360',
'525362',
'525363',
'525364',
'525371',
'106540',
'525537',
'525539',
'525617',
'525690',
'525727',
'525728',
'525765',
'525766',
'525776',
'525777',
'525782',
'525802',
'525803',
'525827',
'520204',
'522527',
'525877',
'525887',
'525903',
'525915',
'525916',
'525918',
'525919',
'525982',
'526347',
'526349',
'526350',
'526584',
'527043',
'527045',
'527361',
'527433',
'527436',
'527466',
'527467',
'527474',
'527510',
'527513',
'527561',
'527665',
'528002',
'528003',
'528015',
'528018',
'528065',
'528066',
'528078',
'528080',
'528097',
'528168',
'528169',
'528195',
'528290',
'12356',
'12357',
'528315',
'528317',
'528320',
'528440',
'528492',
'528585',
'528593',
'528594',
'530997',
'528628',
'528697',
'529105',
'529106',
'529107',
'500227',
'500276',
'500284',
'500286',
'500293',
'529517',
'529545',
'530110',
'500384',
'500442',
'500449',
'500485',
'500527',
'500541',
'500580',
'500618',
'500651',
'500652',
'500699',
'530155',
'530162',
'530288',
'530343',
'530355',
'530391',
'530393',
'500772',
'500773',
'500834',
'500877',
'500901',
'500912',
'500957',
'500973',
'501037',
'501038',
'530672',
'530673',
'530675',
'530689',
'530692',
'530746',
'530995',
'530996',
'14957',
'501157',
'501189',
'501309',
'501339',
'501362',
'501382',
'501424',
'528627',
'531249',
'531258',
'531370',
'531374',
'531377',
'531383',
'531397',
'531407',
'531413',
'531446',
'531483',
'531499',
'501510',
'501607',
'501609',
'501678',
'501689',
'501699',
'501788',
'501812',
'502009',
'502017',
'502024',
'502052',
'502072',
'502076',
'502081',
'502094',
'502095',
'502123',
'502128',
'502130',
'502135',
'502149',
'502182',
'502193',
'502223',
'502224',
'502230',
'502241',
'531633',
'531705',
'531749',
'531839',
'531840',
'503051',
'503054',
'503055',
'503056',
'503057',
'503064',
'LSM116',
'531981',
'531982',
'531983',
'531985',
'532009',
'503178',
'503256',
'503265',
'503266',
'526364',
'530988',
'527120',
'500352',
'530198',
'530336',
'530337',
'530481',
'530737',
'531371',
'531372',
'531373',
'531463',
'540039',
'506023'
]

if __name__ == '__main__':
    main()