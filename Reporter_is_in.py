import pandas as pd

# years = years for which compiled data are available
# weeks are for 2012 - 2014 where only week-by-week data are available
years = range (2008,2013)
week_years = range(2013,2015)
week_numbers = range(69,124)

RePORTER_TRIM_path = 'C:\Users\LIlaJeff\Downloads\RePorter\RePORTER_TRIM.csv'
Residents_path = 'C:\Users\LIlaJeff\Downloads\RePorter\\brig_res.csv'

Residents = pd.read_csv(Residents_path, index_col=False, names =['PI_NAMEs', 'Grad_Year', 'Type', 'Current_Title', 'Current_Institution'], squeeze=True)
RePORTER = pd.read_csv(RePORTER_TRIM_path, index_col=False, header=0, squeeze=True)

print Residents