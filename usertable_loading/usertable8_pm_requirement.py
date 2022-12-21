"""
Set to

'NO PM REQUIRED' = 6
'IN STORAGE' = 8
"""
import config


requirements_dict = {
    'Alvi Ajdini':9,
    'Jonathan Harper':10,
    'Nahila Iqbal':11,
    'Luis Alves':12,
    'David Tao':13,
    'Lawrence Paralejas':14,
    'Shirley Featherston':15,
    'Sophie Peregrine':16,
    'Sally Kirkaldy':17,
    'Uyen Attrill':18,
    'Kannah Vasishtan':19,
    'Alan Glover':21,
    'Susie Wickes':22,
    'Jakson Rounding':23,
    'Mark Bartholomew':24,
    'Bernadette Tucker':25,
    'Janine Boucher':26,
    'Matthew Buck':27
}

def main():
    for asset in config.usertable_8_lst:
        print(f"UPDATE B_EQ1996 SET ID_USERTABLE8=6 WHERE N_IMMA = '{asset}';")

if __name__ == '__main__':
    main()