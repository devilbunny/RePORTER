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
    year = 0
    for data in frame[col]:
        try:
            data = int(data)
            year = data
            GRAD_YEAR.append(None)
        except ValueError:
            GRAD_YEAR.append(year)

    frame['GRAD_YEAR'] = GRAD_YEAR
    return frame

def addphd (frame, col="Col1", PhD_col = 'PhD'):
    '''*DataFrame*, *column = 'Col1'* searches the column for anything
    'phd'-like and then puts either a 'true' or 'false' in a new column called
    PhD_col = 'PhD' '''
    hasphd = []
    for data in frame[col]:
        data = str(data)
        data = data.upper()
        phd = data.count('PHD')
        if phd == 1:
            hasphd.append(True)
        elif phd == 0:
            hasphd.append(False)
        else:
                hasphd.append(None)
    frame['PhD'] = hasphd
    return frame

def ap_or_cp (frame, col = 'Col1'):
    '''*DataFrame*, *column = 'Col1'* searches the column for residency types
    based on them being surrounded by parens and then puts either a 
    whatever is within in a new column called 'AP/CP/?' '''
    apcp = []
    for data in frame[col]:
        try:
            data = str(data)
            data = data.upper()
            data2 = data.split('(')
            data3 = data2[1]
            data4 = data3.split(')')
            isapcp = data4[0]
        except IndexError:
            isapcp = None
        apcp.append(isapcp)       
    frame['AP/CP/?'] = apcp
    return frame

def getname (frame, col = 'Col1'):
     '''*DataFrame*, *column = 'Col1'* returns whatever string is before
     ' MD' in the string in column'''
     names = []
     for data in frame[col]:
         try:
            data = str(data)
            data2 = data.split(' MD')
            name = data2[0]
         except IndexError:
             name = None
         names.append(name)       
     frame['Name'] = names
     return frame

Residents_path = 'C:\Users\JAG\RePORTER\Residencies\mgh.csv'
Fixed_path = 'C:\Users\JAG\RePORTER\Residencies\mgh-fix.csv'
cols = ["Col1", "Col2"]

Residents = pd.read_csv(Residents_path, index_col=False, names = cols)

Residents = addyear(Residents, col="Col1")
Residents = addphd(Residents)
Residents = ap_or_cp(Residents)
Residents = getname(Residents)
Residents = Residents.dropna()
Residents.to_csv(Fixed_path)