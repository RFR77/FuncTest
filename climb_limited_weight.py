from scipy import interpolate
import numpy as np
import pandas as pd
#Open xcel and read the sheet MTOPS
pd.read_excel('page_1-1.xlsx', sheet_name="MTOPS")
#open an empty lists to dump values in.
temp = []
alt = []
wt = []

for row in range(1, sheet.max_row + 1):
    #row has an empty cell next to it, its an altitude and put in alt list.
    if sheet['B'] == 'none':
        z = sheet['A'].value
        alt.append(z)
    else:
        x = sheet['A' + str(row)].value
        y = sheet['B' + str(row)].value
        temp.append(x)
        wt.append(y)
print(alt)
#inputs for calculation
#input_temp = int(input('What is the temperature? '))
#input_alt = int(input('What is the altitude? '))


#This is the first attempt at interpolation, and it works.
#temp = [26, 28, 30, 32, 36, 40]
#alt = [6000, 8000, 10000]

#wt = [[22500, 22500, 22500, 22500, 22500, 22400],
#      [22500, 22500, 22500, 22300, 22200, 22500],
#      [22500, 22500, 22500, 22500, 22500, 22500],
#      [22500, 22500, 22500, 22500, 22500, 22500],
#      [22500, 22500, 22500, 22500, 22500, 22500],
#      [22500, 22500, 22500, 22500, 22500, 22500],
#      [22500, 22500, 22500, 22500, 22500, 22500],
#      [22500, 22500, 22500, 22500, 22500, 21500],
#      [4560, 4760, 4940, 5130, 5540, 7110],
#      [5030, 5250, 5450, 5670, 6120, 8190],
#      [5290, 5510, 5730, 5950, 6420, 8790]]

#f = interpolate.interp2d(temp, wt, fl, kind='linear')

#znew = f(input_temp, input_alt)
#answer is

#print(znew)
