'''MGH wrangle
To wrangle complicated files with year of graduation proceeding several names
Names are of format:
Last, First Degree(s) (ProgramType)", "New Job, Institution, City, State"
'''
import pandas as pd
import numpy as np
from names import split_name


def addyear (frame, years = (2000,20015), col="Col1"):
    '''*DataFrame*, *years=2000-2015* , *column to look at dates = 1*
    takes an input dataframe and adds a 'GRAD_YEAR' column
    then searches down the named column for something that looks year-like,
    copies that number to the year column
    then fills down'''
    GRAD_YEAR = []
    for data in frame[col]:
        try:
            data = data.int()
            GRAD_YEAR.append(data)
        except AttributeError:
            GRAD_YEAR.append(None)
        
    GRAD_YEAR = [name if isinstance(data,int) and int in range(years) else "" for data in frame[col]]
    #csvs = [path for path in paths if path[-3:] == "csv"]
    #reversed_names = [flip_name(name).upper()+';' if isinstance(name, basestring) else name for name in Residents['PI_NAMEs']]
   
Residents_path = 'C:\Users\JAG\RePORTER\Residencies\mgh.csv'
cols = ["Col1", "Col2"]

Residents = pd.read_csv(Residents_path, index_col=False, names = cols)

GRAD_YEAR = []
year = 0
for data in Residents['Col1']:
    try:
        data = int(data)
        year = data
        GRAD_YEAR.append(data)
    except ValueError:
        GRAD_YEAR.append(year)

Residents['GRAD_YEAR'] = GRAD_YEAR


print Residents['Col1'][:5]
print Residents['GRAD_YEAR'][:5]
