

t = ('506108','08/02/2022')

# def convert_date(d):
#     day = d[:2]
#     month= d[3:5]
#     year = d[6:10]
#     return day + month + year

def convert_date(dt):
    d = dt[:2]
    m = dt[3:5]
    y = dt[6:10]
    return(y+m+d)


new_date = convert_date(t[1])
print(new_date)