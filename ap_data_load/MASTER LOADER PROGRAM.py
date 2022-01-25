import med_act_pole
import organisation
import users
import sites
import modality
import suppliers
import technical_dept
import medical_departments
import accounts
import pyodbc
import gmdn
import models
import manufacturers
import assets
import wo_sub_type
import wo_sub_status
import sys

"""
code explanation
'T' means do truncate
'I' means do insert
'TI' means do both
'S' means to skip
"""

def main():
    conn = get_db_connection()

    # set customer for Imperial or Spire
    customer = 'Imperial'
    if customer == 'Imperial':
        fn = "C:\\Users\\212628255\\Documents\\GE\\AssetPlus\\7 Projects\\New Database\\PYTHON TEMPLATE FILE.xlsx"
    elif customer == 'Spire':
        fn = "C:\\Users\\212628255\\Documents\\GE\\AssetPlus\\7 Projects\\New Database\\SPIRE PYTHON TEMPLATE FILE.xlsx"

    # set actions Empty, Load, or Specific
    action = 'Load'
    if action == 'Empty':
        empty_db(conn, fn)
    elif action == 'Load':
        load_db(conn, fn)
    elif action == 'Specific':
        specific(conn, fn)


def get_db_connection():
    # database connection
    server = 'GC0DF7Y2E\SQLEXPRESS'
    database = 'AP10_9'
    username = 'SOPHIE'
    password = 'SOFLOG'
    return pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database +
                   ';UID=' + username + ';PWD=' + password)


def empty_db(conn, fn):
    # users.load(conn, fn, 'T')
    wo_sub_type.load(conn, fn, 'T')
    wo_sub_status.load(conn, fn, 'T')
    modality.load(conn, fn, 'T')
    gmdn.load(conn, fn, 'T')
    suppliers.load(conn, fn, 'T')
    accounts.load(conn, fn, 'T')
    organisation.load(conn, fn, 'T')
    sites.load(conn, fn, 'T')
    med_act_pole.load(conn, fn, 'T')
    medical_departments.load(conn, fn, 'T')
    technical_dept.load(conn, fn,'T')
    manufacturers.load(conn, fn, 'T')
    models.load(conn, fn, 'T')
    suppliers.load(conn, fn, 'T')
    accounts.load(conn, fn, 'T')

def load_db(conn, fn):
    # users.load(conn, fn, 'I')
    wo_sub_type.load(conn, fn, 'I')
    wo_sub_status.load(conn, fn, 'I')
    modality.load(conn, fn, 'I')
    gmdn.load(conn, fn, 'I')
    suppliers.load(conn, fn, 'I')
    accounts.load(conn, fn, 'I')
    organisation.load(conn, fn, 'I')
    sites.load(conn, fn, 'I')
    med_act_pole.load(conn, fn, 'I')
    medical_departments.load(conn, fn, 'I')
    technical_dept.load(conn, fn,'I')
    manufacturers.load(conn, fn, 'I')
    models.load(conn, fn, 'I')
    suppliers.load(conn, fn, 'I')
    accounts.load(conn, fn, 'I')

def specific(conn, fn):
    assets.load(conn, fn, 'S')
    # ****** Settings ******
    # profiles.load(conn, fn)
    users.load(conn, fn, 'S')
    wo_sub_type.load(conn, fn, 'S')
    wo_sub_status.load(conn, fn, 'S')
    # ****** Administrative Structure ******
    organisation.load(conn, fn, 'S')
    sites.load(conn, fn, 'S')
    # responsibility_centers.load(conn, fn)
    # services.load(conn, fn)
    med_act_pole.load(conn, fn, 'S')
    medical_departments.load(conn, fn, 'S')
    technical_dept.load(conn, fn,'S')
    # fun_class
    # ****** Nomenclature ******
    modality.load(conn, fn, 'S')
    gmdn.load(conn, fn, 'S')
    manufacturers.load(conn, fn, 'S')
    models.load(conn, fn, 'S')
    # risk
    # category
    # family
    # operating_hours
    # origin
    # ****** Operating Data ******
    # causes
    # corrective_actions
    # controls
    # technical_fields
    # technical_units
    # suppl_contacts
    # check_list
    # ****** Finance ******
    suppliers.load(conn, fn, 'S')
    # fiscal_period
    accounts.load(conn, fn, 'S')
    # budget

    # ****** Resources & Documents ******
    # training.load()
    # tecnicians.load()
    # document_man




if __name__ == '__main__':
    main()


