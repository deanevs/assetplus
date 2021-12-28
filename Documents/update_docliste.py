


def main():
    nu_doc = 341604
    primaire = 'N_IMMA'
    asset = '504581'
    sql_update = f"UPDATE DOCLISTE SET PRIMAIRE = '{primaire}' ,N_IMMA = '{asset}' WHERE (NU_DOC = '{nu_doc}')"

    print(sql_update)

if __name__ == '__main__':
    main()