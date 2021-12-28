

s = "TEXAS INSTRUMENTS LTD"
print(s)
remove_list = [' LTD', ' LIMITED', ' LLC', ' UK', ' EUROPE', ' SCIENTIFIC', ' MEDICAL', ' EQUIPMENT', ' INSTRUMENTS',
               ' TECHNOLOGY', ' TECHNOLOGIES', ' SYSTEMS', ' INSTRUMENTATION', ' SYSTEM', ' INTERNATIONAL', ' HEALTHCARE']

temp = s
for r in remove_list:
    if r in temp:
        temp = temp.replace(r,'')


print(temp)