


def main():

    N_EF = 'CARDIAC'
    for asset_id in cardiac_list:
        sql = F"UPDATE B_EQ1996 SET N_EF = '{N_EF}' WHERE N_IMMA = '{asset_id}'"
        print(sql)

    # for asset_id in cardiac_hh_list:
    #     sql = F"UPDATE B_EQ1996 SET N_EF = '{N_EF}' WHERE N_IMMA = '{asset_id}'"
    #     print(sql)
    #
    # for asset_id in cardiac_cx_list:
    #     sql = F"UPDATE B_EQ1996 SET N_EF = '{N_EF}' WHERE N_IMMA = '{asset_id}'"
    #     print(sql)

cardiac_list = ['537299',
'537293',
'538943',
'537301',
'537298',
'532420',
'532421',
'535750',
'537296',
'532390',
'535749',
'528192',
'528451',
'537297',
'528298',
'528300',
'528297',
'528299',
'9531',
'527441',
'527425',
'537253',
'527534',
'510490',
'510501',
'510498',
'533408',
'534512',
'532325',
'533407',
'533399',
'532326',
'532327',
'533395',
'533398',
'534511',
'533397',
'533396',
'AP-18952',
'AP-22599',
'AP-22598',
'532328',
'532329',
'533470',
'533471',
'AP-18348',
'AP-18345',
'AP-18347',
'AP-18346',
'507606',
'532332',
'533406',
'533405',
'533404',
'533401',
'532333',
'532334',
'533403',
'533361',
'533408',
'104808',
'104809',
'533407',
'533399',
'202539',
'202541',
'533395',
'533398',
'534511',
'533397',
'533396',
'533773',
'533995',
'533994',
'104825',
'104826',
'533470',
'533471',
'533649',
'533646',
'533648',
'533647',
'206470',
'206326',
'533406',
'533405',
'533404',
'533402',
'533401',
'104819',
'104821',
'104822',
'533403',
'533361'

]

audiology_list = ['AP-19277',
'526459',
'526467',
'539605',
'526463',
'539611',
'526466',
'512353',
'539631',
'517528',
'540269',
'514658',
'512359',
'536019',
'511512',
'512363',
'539610',
'AP-22344',
'AP-19511',
'306753',
'AP-19520',
'536889',
'526211',
'536886',
'536887',
'536890',
'536891',
'536894',
'511509',
'526212',
'AP-19278',
'AP-22047',
'AP-21100',
'AP-21101',
'AP-23369',
'AP-22044',
'AP-22046',
'AP-24420',
'AP-24421',
'512226',
'516542',
'526465',
'539608',
'509574',
'517527',
'536893',
'539575',
'536888',
'514662',
'528459',
'526102',
'514656',
'531220',
'526458',
'536543',
'514660',
'AP-19279',
'AP-19335',
'AP-24587',
'AP-24598',
'AP-24599',
'AP-24627',
'526464',
'526461',
'540268',
'526460',
'AP-24831',
'AP-24627',
'516542',
'AP-25137',
'AP-27076',
'526261',
'527434',
'AP-24518',
'AP-24519',
'543151',
'AP-24520',
'AP-24521',
'AP-24596',
'AP-24527',
'AP-24531',
'543154',
'543150',
'543155',
'535354',
'535579',
'AP-21102',
'AP-24503',
'526262',
'511511',
'526263',
'543153',
'543156',
'12939',
'530484',
'530512',
'AP-24533',
'AP-24630',
'509538',
'509538',
'530511',
'AP-24628',
'AP-24629',
'509533',
'509573',
'509539',
'509534',
'509578',
'509536',
'511510',
'AP-17294',
'504989',
'538413',
'511309',
'511708',
'528798',
'203033',
'520531',
'520530',
'517839',
'520582',
'517836']

cardiac_sm_wrong_list = ['567491',
'525421',
'557175',
'527346',
'527442',
'528210',
'527443',
'528211',
'528214',
'527341',
'528400',
'527536',
'510548',
'528415',
'525434',
'525429',
'510549',
'515444',
'510546',
'525431',
'525441',
'525409',
'527534',
'526831',
'543289',
'527540',
'537253',
'511310',
'557255',
'519449',
'511399',
'543543',
'511727',
'557128',
'557124',
'511311',
'511312',
'516683',
'516685',
'511728',
'557123',
'557127',
'557303',
'526091',
'526184',
'526188',
'553679',
'553680',
'506490',
'526826',
'542509',
'528212',
'528223',
'528906',
'528907',
'528911',
'530433',
'542832',
'567490',
'557428']

cardiac_sm_list = ['506490',
'510546',
'510548',
'510549',
'511310',
'511311',
'511312',
'AP-19371',
'AP-18101',
'AP-18100',
'515444',
'516683',
'516685',
'519449',
'525409',
'525421',
'525429',
'525431',
'525434',
'525441',
'526091',
'526184',
'526188',
'526826',
'528207',
'527341',
'527346',
'527442',
'527443',
'527534',
'527536',
'527540',
'528210',
'528211',
'528212',
'AP-19370',
'528223',
'528400',
'528415',
'528906',
'528907',
'528911',
'530433',
'537253',
'AP-19577',
'AP-23313',
'543289',
'543543',
'AP-19227',
'AP-19228',
'AP-18102',
'AP-18104',
'AP-18105',
'AP-18103',
'AP-18263',
'307618',
'AP-18603',
'AP-22697',
'AP-23321',
'AP-23322']

cardiac_hh_list = ['507566',
'521733',
'526280',
'520015',
'507565',
'507598',
'507573',
'507695',
'507579',
'507597',
'507688',
'521695',
'521710',
'507567',
'507693',
'534698',
'534699',
'VH001353HI',
'520028',
'520029',
'507577',
'520014',
'507570',
'520019',
'507687',
'202383',
'507568',
'520023',
'520064',
'520066',
'520067',
'520020',
'520021',
'507571',
'520017',
'520018',
'507564',
'521734',
'521693',
'521735',
'521736',
'501741',
'501742',
'506464',
'48585',
'520016',
'AP-24202',
'AP-24203',
'AP-19448',
'AP-19063',
'AP-19066',
'AP-19064',
'AP-19067',
'AP-19068',
'AP-19069',
'AP-20171',
'AP-20173',
'AP-20172',
'AP-20174',
'AP-20176',
'520016',
'AP-20177',
'AP-20178',
'AP-20175',
'AP-20179',
'AP-20166',
'AP-20168',
'AP-20167',
'AP-20169']

cardiac_cx_list = ['AP-24117',
'539359',
'AP-23724',
'501575',
'510967',
'531330',
'514691',
'506626',
'503550',
'506934',
'514524',
'513426',
'531617',
'531619',
'531618',
'526219',
'526218',
'529455',
'531333',
'532351',
'538063',
'536160',
'538052',
'AP-19276',
'105029',
'514689',
'538052',
'532335',
'538064',
'532336',
'538048',
'538049',
'532339',
'538059',
'538061',
'538046',
'538056',
'536160',
'536159',
'532347',
'538057',
'539594',
'536061',
'538047',
'532353',
'532355',
'538053',
'538060',
'532358',
'532359',
'532360',
'538062',
'532361',
'532362',
'514510',
'305712',
'531619',
'519193',
'519192',
'528466',
'528469',
'526736',
'536807',
'528526',
'528164',
'536817',
'536805',
'528127',
'528128',
'536804'
]


if __name__ == '__main__':
    main()