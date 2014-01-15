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

RePorter_fix_path = "C:\Users\JAG\RePORTER\Output\RePORT_Append_Titles.csv"
Residents_plus_grants_path = "C:\Users\JAG\RePORTER\Output\RePORT_Append_Titles-f.csv"


RWG_fix = pd.read_csv(RePorter_fix_path, sep=',' , index_col = False, header =0)

#RWG_sum = RWG_fix.groupby('PI_NAMEs')['TOTAL_COST'].sum()


RWG_pivot = RWG_fix.pivot_table('TOTAL_COST', rows ='PI_NAMEs', cols ='ACTIVITY', aggfunc = 'sum')
RWG_pivot['PI_NAMEs'] = RWG_pivot.index

RWG_fix = RWG_fix.merge(RWG_pivot, how = 'outer')

RWG_fix.to_csv(Residents_plus_grants_path, sep = ',' , index = False)




