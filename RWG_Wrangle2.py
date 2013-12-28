#RWG wrangle takes a csv of residents with grants and does some operations
# 1. it strips out non F, K, or R grants
# at this point the remaining grants should be manually verified
# 2. it determines the earliest year when residents received a grant
# the list is then merged back into the original list of residents, so that for each resident, 
# the earliest year to receive each grant, and the total cost is incorporated
# This is followed by RWG analyze


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Residents_path = "C:\Users\JAG\RePORTER\Residencies\perimatch-fix.csv"
RWG_fix_path = "C:\Users\JAG\RePORTER\Residencies\perimatch-RWG-f2.csv"
Residents_plus_grants_path = "C:\Users\JAG\RePORTER\Residencies\perimatch-G.csv"

Residents = pd.read_csv(Residents_path, sep = ',' , index_col = False, header =0, squeeze = True)
RWG_fix = pd.read_csv(RWG_fix_path, sep=',' , index_col = False, header =0)

RWG_sum = RWG_fix.groupby('Name').sum()
RWG_sum['Name'] = RWG_sum.index
RWG_sum = RWG_sum[['Name','TOTAL_COST']]

RWG_pivot = RWG_fix.pivot_table('Years_to_grant', rows ='Name', cols ='ACTIVITY', aggfunc = 'min')
RWG_pivot['Name'] = RWG_pivot.index
RWG_pivot = RWG_pivot.merge(RWG_sum)

RWG_fix = Residents.merge(RWG_pivot, how = 'outer')
RWG_fix.to_csv(Residents_plus_grants_path, sep = ',' , index = False)




