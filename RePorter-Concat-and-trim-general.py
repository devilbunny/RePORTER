import pandas as pd
import os

# years = years for which compiled data are available
# weeks are for 2012 - 2014 where only week-by-week data are available
years = range (2008,2013)
week_years = range(2013,2015)
week_numbers = range(69,124)
data_path = 'C:\Users\JAG\RePORTER\\'
results_path = 'C:\Users\JAG\RePORTER\\'
results_file = 'RePORTER_Trim.csv'
columns = ['APPLICATION_ID', 'ACTIVITY', 'PI_NAMEs', 'ORG_NAME', 'ORG_CITY', 'BUDGET_START']


data_list = []
data_list = os.listdir(data_path)
print data_list
for name in data_list:
    frame = pd.read_csv(data_path + name, header = 0, sep = ',')
    trim_frame = frame(columns)
    trim_frame.to_csv(results_path + results_file, sep = ',' , index = False, mode = 'a')