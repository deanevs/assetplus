# import regex
import re

p = re.compile('(?![ -~]).')

s = "conduction from the patient's skin to the SenTec TC Sensors."

s = s.replace("'", "")

print(s)




