
sql_manufacturer = 'SELECT [MA_NOM] AS MANUFACTURER, \
                    [DATE_REFOR] AS RETIRED\
                    FROM [AssetPlus].[dbo].[MARQUES] \
                    WHERE DATE_REFOR is NULL'

# AssetPlus GMDN table
gmdn_select = 'SELECT [N_NOM_CNEH],' \
           '[NOM],' \
           '[NOM2],' \
           '[F_SPECC],' \
           '[F_SPECL2],' \
           '[EQ_AMT_COM],' \
           '[CRIT_ACT],' \
           '[REMP_PRIX],' \
           '[RISKCODE],' \
           '[ECR_MODCODE] \
            FROM [AssetPlus].[dbo].[EQ_CNEH]'

gmdn_insert = 'INSERT INTO EQ_CNEH (N_NOM_CNEH, NOM, NOM2) VALUES'

sql_model = 'SELECT [TP_TYPE] AS MODEL, \
                [MARQUE] AS MANUFACTURER, \
                [FOUR_TYPE] AS SUPPLIER, \
                [CNEH_TYPE] AS GMDN_CODE, \
                [NOM2] AS MODEL_ALT_NAME, \
                [ASSET_PART_TYPE] AS ASSET_TYPE, \
                [REMP_PRIX] AS  REP_COST \
            FROM [AssetPlus].[dbo].[TYPES]'

# model, manufacturer, gmdn_id, name_2,
sql_model_update = """INSERT INTO TYPES 
                   (TP_TYPE, MARQUE, CNEH_TYPE, NOM2, ASSET_PART_TYPE, REMP_PRIX) 
                   VALUES ({},{},{},{},{},{})"""

# now create sql query
# sql = "INSERT INTO EQ_CNEH ('N_NOM_CNEH','NOM') VALUES "
# for item in gmdn:
#     sql = sql + str(item) + ',\n'

sql_man_insert = "INSERT INTO MARQUES ([MA_NOM]) VALUES (%s)"



# map excel columns to variables
excel_ult_map = {
    'gmdn_by_use':'GMDN By Use',
    'gmdn_name':'GMDN Preferred Term',
    'gmdn_id':'GMDN_CODE',
    'prim_di':'Primary DI',
    'manufacturer':'Company',
    'brand':'Brand',
    'model':'Version',
    'desc':'Description'
}

# map variables to TYPES aka MODELS table
ap_types_map = {
    'model':'TP_TYPE',      # version
    'manufacturer':'MARQUE',    # company
    'supplier_code':'FOUR_TYPE',    # set=2 'TBD'
    'gmdn_code':'CNEH_TYPE',    # gmdn_code
    'name_2':'NOM2',    # brand & prim_DI & description
    'asset_or_part' : 'ASSET_PART_TYPE', # asset=1, part=2 (set='1')
    'rep_cost':'REMP_PRIX',  # (set=0)
    'rfid':'IS_RFID_TAG'   # 0=No, 1=Yes (set='0')
}

# map variables to EQ_CNEH aka GMDN table
ap_gmdn_map = {
    'gmdn_code':'N_NOM_CNEH',   # gmdn_code
    'gmdn_name':'NOM',  # gmdn_preferred_term
    'gmdn_alt_name': 'NOM2',    # gmdn_by_use
    'ct_code':'F_SPECC',    # group -> collective term? CT1234 NOTE only 3 chars!!
    'ct_name':'F_SPECL2',   #
}

ap_manufacturer_map = {
    'manufacturer':'MA_NOM',
    'retired':'DATE_REFOR'
}

