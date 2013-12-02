import pandas as pd

# years = years for which compiled data are available
# weeks are for 2012 - 2014 where only week-by-week data are available
years = range (2008,2013)
week_years = range(2013,2015)
week_numbers = range(69,124)
data_path = 'C:\Users\LIlaJeff\Documents\GitHub\RePORTER\Data\\'
results_path = 'C:\Users\LIlaJeff\Documents\GitHub\RePORTER\Results\\'
results_file = 'RePORTER_Trim.csv'
columns = ['APPLICATION_ID', 'ACTIVITY', 'PI_NAMEs', 'ORG_NAME', 'ORG_CITY', 'BUDGET_START']


data_list = []
data_list = %dirs
'''
#Block to concat the yearly series - this is done'
for year in years:
    path_year = path + '\RePORTER_PRJ_C_FY%d.csv' % year
    print path_year
    frame = pd.read_csv(path_year, index_col=False, header=0, squeeze=True)
    trim_frame = frame[['APPLICATION_ID', 'ACTIVITY', 'PI_NAMEs', 'ORG_NAME', 'ORG_CITY']]
    trim_frame.to_csv(path + '\RePORTER_Trim.csv', sep = ',' , index = False, mode = 'a')


#this loop iterates through each week in each week_year, will generate lots of erros
for year in week_years:
    path_year = path + '\RePORTER_PRJ_C_FY' + str(year)
    for week in week_numbers:
        path_year_week = str(path_year) + "_" + str(week) + '.csv'
        print path_year_week
        try:
            frame = pd.read_csv(path_year_week, index_col=False, header=0, squeeze=True)
            trim_frame = frame[['APPLICATION_ID', 'ACTIVITY', 'PI_NAMEs', 'ORG_NAME', 'ORG_CITY']]
            trim_frame.to_csv(path + '\RePORTER_Trim.csv', sep = ',' , index = False, mode = 'a')

        except:
           print "exception" 
               
print "done"

pd.read_csv(path + "/RePORTER_ALL.csv", nrows = 5, ncols = 5)
total_births = names.pivot_table('births', rows = 'year', cols = 'sex', aggfunc=sum)

def add_prop(group):
        #integer division floors
        births = group.births.astype(float)
        group['prop'] = births / births.sum()
        return group
    
names = names.groupby(['year','sex']).apply(add_prop)
'''