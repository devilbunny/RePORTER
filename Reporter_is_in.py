import pandas as pd
import numpy as np
from names import split_name
# years = years for which compiled data are available
# weeks are for 2012 - 2014 where only week-by-week data are available
years = range (2008,2013)
week_years = range(2013,2015)
week_numbers = range(69,124)

#Make data frames from .csvs and does basic trim
RePORTER_TRIM_path = 'C:\Users\LIlaJeff\Downloads\RePorter\RePORTER_TRIM.csv'
Residents_path = 'C:\Users\LIlaJeff\Downloads\RePorter\\brig_res.csv'
Residents_With_Grants_path = "C:\Users\LIlaJeff\Downloads\RePorter\RWG.csv"

# these are the columns we care about
Residents = pd.read_csv(Residents_path, index_col=False, names = ['PI_NAMEs', 'Grad_Year', 'Type', 'Current_Title', 'Current_Institution'], squeeze=True, na_values = ["NAN", "Na", " ", ""])
RePORTER = pd.read_csv(RePORTER_TRIM_path, index_col=False, header=0, squeeze=True)

def flip_name(name):
    ''' takes a string in the format of Firstname Lastname and returns a string of Lastname, Firstname, uses the names function
    from billy to make a tuple and then rearranges it.'''  
    first_last = split_name(name)
    if first_last is not None:
        firstname, lastname = first_last
        return lastname + ", " + firstname
    else:
        return name



reversed_names = [flip_name(name).upper()+';' if isinstance(name, basestring) else name for name in Residents['PI_NAMEs']]
Residents['PI_NAMEs'] = reversed_names

Residents = Residents.dropna()

Residents_With_Grants = Residents.merge(RePORTER)
Residents_With_Grants.to_csv(Residents_With_Grants_path, sep = ',' , index = False)
