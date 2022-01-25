"""
All you need is a list of work order numbers that need to be converted to archived.
Note this is in integer format
"""

def main():
    to_be_converted = [157162]

    for wo in to_be_converted:
        print(convert_to_archived(wo))
        print("--******************************************")




# SQL required to convert work order from in-progress to archived
def convert_to_archived(wo_num):
    """
    1. Copy EN_COURS to FT1996
    2. Delete from EN_COURS
    :return: sql_out - the SQL text generated
    """
    status = 2

    sql_insert = f"INSERT INTO B_FT1996 (NU_INT,NU_BON_C,NU_IMM,N_UF,N_EF,DA_AP,HE_AP,DA_INT,HE_INT,DA_HS,HE_HS,DA_DIS,HE_DIS,DA_FIN,HE_FIN,URG,DISP_EF_AT,DISP_AP_AT,COMPT," \
                 f"CADRE,NHE,C_FAC,COD_SAIS,PD1_HT,PD2_HT,MO_HT,DEP_HT,TOT_TTC,HINT,CDEP,PIEC,CINT,OBSERV,ANA_DEF,REM_A_DISP,R_A_D_SUIT,CODE_FOUR,CODE_TECHN,FOURNI,N_MARCHE," \
                 f"M_AN_EFFET,OBSERV2,E_REFER,DIT_TCMN,INT_STATUT,INT_CM,INT_CAUSE,INT_REMED,INT_CONTRA,INTERLOC,PHONE,HLIMIT,W_NATURE,NHEE,TECHN_EXT,OBSERV3,NU_COMPTE," \
                 f"DATE_SYST,DA_REC,HE_REC,DELAI,CODE_DELAI,DA_HDELAI,N_DEVIS,N_FACTURE,MT_ENGAG,DA_RECP,TOT_INT,DIV_INT,DIV_EXT,LIB_CADRE,LIB_STATUT,PAR1,PAR2,PAR3,PAR4," \
                 f"PAR5,FK_CONTACT_PERSON_ID,FK_ADDRESS_ID,DATE_OF_NU_BON_C,INSERT_DATE,UPDATE_DATE,RI_SUIVI_CM,RI_SUIVI_TECHN,N_MARCHE_PUBLIQUE,DATE_PREV,PERIODELA,DA_DD,DA_DR," \
                 f"DA_DA,FROM_WEB,ESTIMATEDDURATION,GENERIC,GENERIC_SEQ,TOLERANCE,TOLERANCE_DMY,FILLER1,FILLER2,FILLER3,FILLER4,FILLER5,V_FONC,MODE_CALCUL_PM,PERIODICITY_OCCURRENCE," \
                 f"PERIODICITY_DMY,FILLER6,FILLER7,ID_USERTABLE1,ID_USERTABLE2,ID_USERTABLE3,ID_USERTABLE4,ID_USERTABLE5,NB_ASSET_GENERIC,NB_TOT_ASSET_GENERIC,AMOUNT_QUOTE," \
                 f"FK_BUDGET_AN_EXO,WO_PARENT_NUMBER,WO_TREE_PATH,WO_TREE_LEVEL,QUICK_WO_USE,QUICK_WO_RESULT,WO_UPDATED_HISTORIC,FILLER8,FILLER9,FILLER10,FILLER11,FILLER12," \
                 f"USER_BUYER_CODE,ID_USERTABLE1_WO,ID_USERTABLE2_WO,ID_USERTABLE3_WO,ID_USERTABLE4_WO,ID_USERTABLE5_WO,CALLER_EMAIL,IS_CALLER_NOTIFIED,MAXDATERESPONSE," \
                 f"MAXTIMERESPONSE,OLD_COUNTER,PERIODE,IS_DIGITAL_SIGN,IS_WO_SIGN_MANDATORY,COMPETENCY_IS_ACTIVATED,ID_USERTABLE6,ID_USERTABLE7,ID_USERTABLE8,WO_FORWARD_BY_TD," \
                 f"IS_DECONTAMINATED,RESPONSE_TIME_CALCUL_MODE,UDI,CALL_CREATOR,AUTODISPATCH_NOTIF_STATUS,PHONE_MOBILE,FK_PREV_EQP,DATE_PREV_CALCULATED,WO_GE_WONUM,WO_USER_CREATOR," \
                 f"FK_PREP_ID,ORDER_AMOUNT,TOT_TTC_PLUS_ORD_AM,CALIBRATION_WO,CALIBRATION_DATE,CALIBRATION_NEXT_DATE,CALIBRATION_WO_STATUS) SELECT NU_INT,NU_BON_C,NU_IMM,N_UF,N_EF," \
                 f"DA_AP,HE_AP,DA_INT,HE_INT,DA_HS,HE_HS,DA_DIS,HE_DIS,DA_FIN,HE_FIN,URG,DISP_EF_AT,DISP_AP_AT,COMPT,CADRE,NHE,C_FAC,COD_SAIS,PD1_HT,PD2_HT,MO_HT,DEP_HT,TOT_TTC,HINT," \
                 f"CDEP,PIEC,CINT,OBSERV,ANA_DEF,REM_A_DISP,R_A_D_SUIT,CODE_FOUR,CODE_TECHN,FOURNI,N_MARCHE,M_AN_EFFET,OBSERV2,E_REFER,DIT_TCMN,INT_STATUT,INT_CM,INT_CAUSE,INT_REMED," \
                 f"INT_CONTRA,INTERLOC,PHONE,HLIMIT,W_NATURE,NHEE,TECHN_EXT,OBSERV3,NU_COMPTE,DATE_SYST,DA_REC,HE_REC,DELAI,CODE_DELAI,DA_HDELAI,N_DEVIS,N_FACTURE,MT_ENGAG,DA_RECP," \
                 f"TOT_INT,DIV_INT,DIV_EXT,LIB_CADRE,LIB_STATUT,PAR1,PAR2,PAR3,PAR4,PAR5,FK_CONTACT_PERSON_ID,FK_ADDRESS_ID,DATE_OF_NU_BON_C,INSERT_DATE,UPDATE_DATE,RI_SUIVI_CM," \
                 f"RI_SUIVI_TECHN,N_MARCHE_PUBLIQUE,DATE_PREV,PERIODELA,DA_DD,DA_DR,DA_DA,FROM_WEB,ESTIMATEDDURATION,GENERIC,GENERIC_SEQ,TOLERANCE,TOLERANCE_DMY,FILLER1,FILLER2," \
                 f"FILLER3,FILLER4,FILLER5,V_FONC,MODE_CALCUL_PM,PERIODICITY_OCCURRENCE,PERIODICITY_DMY,FILLER6,FILLER7,ID_USERTABLE1,ID_USERTABLE2,ID_USERTABLE3,ID_USERTABLE4," \
                 f"ID_USERTABLE5,NB_ASSET_GENERIC,NB_TOT_ASSET_GENERIC,AMOUNT_QUOTE,FK_BUDGET_AN_EXO,WO_PARENT_NUMBER,WO_TREE_PATH,WO_TREE_LEVEL,QUICK_WO_USE,QUICK_WO_RESULT," \
                 f"WO_UPDATED_HISTORIC,FILLER8,FILLER9,FILLER10,FILLER11,FILLER12,USER_BUYER_CODE,ID_USERTABLE1_WO,ID_USERTABLE2_WO,ID_USERTABLE3_WO,ID_USERTABLE4_WO," \
                 f"ID_USERTABLE5_WO,CALLER_EMAIL,IS_CALLER_NOTIFIED,MAXDATERESPONSE,MAXTIMERESPONSE,OLD_COUNTER,PERIODE,IS_DIGITAL_SIGN,IS_WO_SIGN_MANDATORY,COMPETENCY_IS_ACTIVATED," \
                 f"ID_USERTABLE6,ID_USERTABLE7,ID_USERTABLE8,WO_FORWARD_BY_TD,IS_DECONTAMINATED,RESPONSE_TIME_CALCUL_MODE,UDI,CALL_CREATOR,AUTODISPATCH_NOTIF_STATUS,PHONE_MOBILE," \
                 f"FK_PREV_EQP,DATE_PREV_CALCULATED,WO_GE_WONUM,WO_USER_CREATOR,FK_PREP_ID,ORDER_AMOUNT,TOT_TTC_PLUS_ORD_AM,CALIBRATION_WO,CALIBRATION_DATE,CALIBRATION_NEXT_DATE," \
                 f"CALIBRATION_WO_STATUS FROM EN_COURS WHERE NU_INT='{wo_num}'\n\n"

    sql_delete = f"DELETE FROM EN_COURS WHERE NU_INT= '{wo_num}'\n\n" \

    sql_out = sql_insert + sql_delete

    return sql_out


def convert_to_inprogress(wo_num):
    """
    1. Copy FT1996 TO EN_COURS
    2. Delete from FT1996
    :return: sql_out - the SQL text generated
    """
    status = ''

    sql_insert = f"INSERT INTO EN_COURS (NU_INT,NU_BON_C,NU_IMM,N_UF,N_EF,DA_AP,HE_AP,DA_INT,HE_INT,DA_HS,HE_HS,DA_DIS,HE_DIS,DA_FIN,HE_FIN,URG,DISP_EF_AT,DISP_AP_AT,COMPT," \
                 f"CADRE,NHE,C_FAC,COD_SAIS,PD1_HT,PD2_HT,MO_HT,DEP_HT,TOT_TTC,HINT,CDEP,PIEC,CINT,OBSERV,ANA_DEF,REM_A_DISP,R_A_D_SUIT,CODE_FOUR,CODE_TECHN,FOURNI,N_MARCHE," \
                 f"M_AN_EFFET,OBSERV2,E_REFER,DIT_TCMN,INT_STATUT,INT_CM,INT_CAUSE,INT_REMED,INT_CONTRA,INTERLOC,PHONE,HLIMIT,W_NATURE,NHEE,TECHN_EXT,OBSERV3,NU_COMPTE," \
                 f"DATE_SYST,DA_REC,HE_REC,DELAI,CODE_DELAI,DA_HDELAI,N_DEVIS,N_FACTURE,MT_ENGAG,DA_RECP,TOT_INT,DIV_INT,DIV_EXT,LIB_CADRE,LIB_STATUT,PAR1,PAR2,PAR3,PAR4," \
                 f"PAR5,FK_CONTACT_PERSON_ID,FK_ADDRESS_ID,DATE_OF_NU_BON_C,INSERT_DATE,UPDATE_DATE,RI_SUIVI_CM,RI_SUIVI_TECHN,N_MARCHE_PUBLIQUE,DATE_PREV,PERIODELA,DA_DD,DA_DR," \
                 f"DA_DA,FROM_WEB,ESTIMATEDDURATION,GENERIC,GENERIC_SEQ,TOLERANCE,TOLERANCE_DMY,FILLER1,FILLER2,FILLER3,FILLER4,FILLER5,V_FONC,MODE_CALCUL_PM,PERIODICITY_OCCURRENCE," \
                 f"PERIODICITY_DMY,FILLER6,FILLER7,ID_USERTABLE1,ID_USERTABLE2,ID_USERTABLE3,ID_USERTABLE4,ID_USERTABLE5,NB_ASSET_GENERIC,NB_TOT_ASSET_GENERIC,AMOUNT_QUOTE," \
                 f"FK_BUDGET_AN_EXO,WO_PARENT_NUMBER,WO_TREE_PATH,WO_TREE_LEVEL,QUICK_WO_USE,QUICK_WO_RESULT,WO_UPDATED_HISTORIC,FILLER8,FILLER9,FILLER10,FILLER11,FILLER12," \
                 f"USER_BUYER_CODE,ID_USERTABLE1_WO,ID_USERTABLE2_WO,ID_USERTABLE3_WO,ID_USERTABLE4_WO,ID_USERTABLE5_WO,CALLER_EMAIL,IS_CALLER_NOTIFIED,MAXDATERESPONSE," \
                 f"MAXTIMERESPONSE,OLD_COUNTER,PERIODE,IS_DIGITAL_SIGN,IS_WO_SIGN_MANDATORY,COMPETENCY_IS_ACTIVATED,ID_USERTABLE6,ID_USERTABLE7,ID_USERTABLE8,WO_FORWARD_BY_TD," \
                 f"IS_DECONTAMINATED,RESPONSE_TIME_CALCUL_MODE,UDI,CALL_CREATOR,AUTODISPATCH_NOTIF_STATUS,PHONE_MOBILE,FK_PREV_EQP,DATE_PREV_CALCULATED,WO_GE_WONUM,WO_USER_CREATOR," \
                 f"FK_PREP_ID,ORDER_AMOUNT,TOT_TTC_PLUS_ORD_AM,CALIBRATION_WO,CALIBRATION_DATE,CALIBRATION_NEXT_DATE,CALIBRATION_WO_STATUS) SELECT NU_INT,NU_BON_C,NU_IMM,N_UF,N_EF," \
                 f"DA_AP,HE_AP,DA_INT,HE_INT,DA_HS,HE_HS,DA_DIS,HE_DIS,DA_FIN,HE_FIN,URG,DISP_EF_AT,DISP_AP_AT,COMPT,CADRE,NHE,C_FAC,COD_SAIS,PD1_HT,PD2_HT,MO_HT,DEP_HT,TOT_TTC,HINT," \
                 f"CDEP,PIEC,CINT,OBSERV,ANA_DEF,REM_A_DISP,R_A_D_SUIT,CODE_FOUR,CODE_TECHN,FOURNI,N_MARCHE,M_AN_EFFET,OBSERV2,E_REFER,DIT_TCMN,INT_STATUT,INT_CM,INT_CAUSE,INT_REMED," \
                 f"INT_CONTRA,INTERLOC,PHONE,HLIMIT,W_NATURE,NHEE,TECHN_EXT,OBSERV3,NU_COMPTE,DATE_SYST,DA_REC,HE_REC,DELAI,CODE_DELAI,DA_HDELAI,N_DEVIS,N_FACTURE,MT_ENGAG,DA_RECP," \
                 f"TOT_INT,DIV_INT,DIV_EXT,LIB_CADRE,LIB_STATUT,PAR1,PAR2,PAR3,PAR4,PAR5,FK_CONTACT_PERSON_ID,FK_ADDRESS_ID,DATE_OF_NU_BON_C,INSERT_DATE,UPDATE_DATE,RI_SUIVI_CM," \
                 f"RI_SUIVI_TECHN,N_MARCHE_PUBLIQUE,DATE_PREV,PERIODELA,DA_DD,DA_DR,DA_DA,FROM_WEB,ESTIMATEDDURATION,GENERIC,GENERIC_SEQ,TOLERANCE,TOLERANCE_DMY,FILLER1,FILLER2," \
                 f"FILLER3,FILLER4,FILLER5,V_FONC,MODE_CALCUL_PM,PERIODICITY_OCCURRENCE,PERIODICITY_DMY,FILLER6,FILLER7,ID_USERTABLE1,ID_USERTABLE2,ID_USERTABLE3,ID_USERTABLE4," \
                 f"ID_USERTABLE5,NB_ASSET_GENERIC,NB_TOT_ASSET_GENERIC,AMOUNT_QUOTE,FK_BUDGET_AN_EXO,WO_PARENT_NUMBER,WO_TREE_PATH,WO_TREE_LEVEL,QUICK_WO_USE,QUICK_WO_RESULT," \
                 f"WO_UPDATED_HISTORIC,FILLER8,FILLER9,FILLER10,FILLER11,FILLER12,USER_BUYER_CODE,ID_USERTABLE1_WO,ID_USERTABLE2_WO,ID_USERTABLE3_WO,ID_USERTABLE4_WO," \
                 f"ID_USERTABLE5_WO,CALLER_EMAIL,IS_CALLER_NOTIFIED,MAXDATERESPONSE,MAXTIMERESPONSE,OLD_COUNTER,PERIODE,IS_DIGITAL_SIGN,IS_WO_SIGN_MANDATORY,COMPETENCY_IS_ACTIVATED," \
                 f"ID_USERTABLE6,ID_USERTABLE7,ID_USERTABLE8,WO_FORWARD_BY_TD,IS_DECONTAMINATED,RESPONSE_TIME_CALCUL_MODE,UDI,CALL_CREATOR,AUTODISPATCH_NOTIF_STATUS,PHONE_MOBILE," \
                 f"FK_PREV_EQP,DATE_PREV_CALCULATED,WO_GE_WONUM,WO_USER_CREATOR,FK_PREP_ID,ORDER_AMOUNT,TOT_TTC_PLUS_ORD_AM,CALIBRATION_WO,CALIBRATION_DATE,CALIBRATION_NEXT_DATE," \
                 f"CALIBRATION_WO_STATUS FROM EN_COURS WHERE NU_INT='{wo_num}'\n\n"

    sql_update_status = f"UPDATE EN_COURS SET INT_STATUT = '2' WHERE NU_INT = '{wo_num}'\n\n"

    sql_delete = f"DELETE FROM B_FT1996 WHERE NU_INT= '{wo_num}'\n\n" \

    sql_out = sql_insert + sql_delete + sql_update_status

    return sql_out

if __name__ == '__main__':
    main()