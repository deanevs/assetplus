import medical_activity_poles
import organisation
import users
import sites
import modality
import suppliers
import technical_dept
import medical_departments
import accounts_old
import pyodbc
import gmdn_old
import models
import manufacturers
import assets
import wo_sub_type
import wo_sub_status



def get_db_connection():
    # database connection
    server = 'GC0DF7Y2E\SQLEXPRESS'
    database = 'AP10_9'
    username = 'SOPHIE'
    password = 'SOFLOG'
    return pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database +
                   ';UID=' + username + ';PWD=' + password)


def truncate_all(conn, fn):
    users.load(conn, fn, 'S')
    wo_sub_type.load(conn, fn, 'S')
    wo_sub_status.load(conn, fn, 'S')
    # organisation.load(conn, fn)
    # sites.load(conn, fn)
    # responsibility_centers.load(conn, fn)
    # services.load(conn, fn)
    # medical_activity_poles.load(conn, fn)
    # medical_departments.load(conn, fn)
    # technical_dept.load(conn, fn)
    # fun_class
    modality.load(conn, fn, 'S')
    # gmdn.load(conn, fn)
    # manufacturers.load(conn, fn)
    # models.load(conn, fn)
    suppliers.load(conn, fn, 'S')
    # fiscal_period
    accounts_old.load(conn, fn, 'S')
    technicians.load(conn, fn, 'T')


def main():
    conn = get_db_connection()
    fn = "C:\\Users\\212628255\\Documents\\GE\\AssetPlus\\7 Projects\\New Database\\PYTHON TEMPLATE FILE.xlsx"

    """
    code explanation
    'T' means do truncate
    'I' means do insert
    'TI' means do both
    'S' means to skip
    """

    # assets.load(conn, fn, 'S')

    # ****** Settings ******
    # profiles.load(conn, fn)
    users.load(conn, fn, 'S')
    wo_sub_type.load(conn, fn, 'S')
    wo_sub_status.load(conn, fn, 'S')

    # ****** Administrative Structure ******
    # organisation.load(conn, fn)
    # sites.load(conn, fn)
    # responsibility_centers.load(conn, fn)
    # services.load(conn, fn)
    # medical_activity_poles.load(conn, fn)
    # medical_departments.load(conn, fn)
    # technical_dept.load(conn, fn)
    # fun_class

    # ****** Nomenclature ******
    modality.load(conn, fn, 'S')
    # gmdn.load(conn, fn)
    # manufacturers.load(conn, fn)
    # models.load(conn, fn)
    # risk
    #       category
    #       family
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
    accounts_old.load(conn, fn, 'S')
    # budget

    # ****** Resources & Documents ******
    # training.load()
    # tecnicians.load()
    # document_man


if __name__ == '__main__':
    main()


