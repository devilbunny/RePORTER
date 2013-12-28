'''wustl wrangle
To wrangle complicated files with year of graduation proceeding several names
Names are of format:
Last, First Degree(s) (ProgramType)", "New Job, Institution, City, State"
'''
import pandas as pd
import numpy as np
from names import split_name

Residents_path = 'C:\Users\JAG\RePORTER\Residencies\wustl.csv'
Fixed_path = 'C:\Users\JAG\RePORTER\Residencies\wustl-fix.csv'
cols = ['Col1', 'APCP', 'Med School', 'Years in', 'Col2']

def addyear (frame, years = (2000,20015), col="Col1"):
    '''*DataFrame*, *years=2000-2015* , *column to look at dates = Col1*
    takes an input dataframe and adds a 'GRAD_YEAR' column
    then searches down the named column for something that looks year-like,
    copies that number to the year column
    then fills down'''
    GRAD_YEAR = []
    year = 0
    for data in frame[col]:
        try:
            data = str(data)
            data = data[-4:]
        except ValueError:
            GRAD_YEAR.append(data)
        try:
            data = int(data)
            year = data
            GRAD_YEAR.append(year)
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
            data2 = data.split(', MD')
            name = data2[0]
         except IndexError:
             name = None
         names.append(name)       
     frame['Name'] = names
     return frame

def unstack3 (series):
    '''*series*, takes a column and unstacks the cells,
    merging each 3 cells'''
    newseries = series
    runner = 0
    goal = series.count()-1
    print goal
    while runner < (goal-3):
        runner2 = runner +1
        runner3 = runner +2
        newdeet = str(series[runner]) + ' ' + str(series[runner2]) + ' ' + str(series[runner3])
        newseries[runner] = newdeet
        runner = runner + 1

    return newseries

def flip_name(name):
    ''' takes a string in the format of Firstname Lastname and returns a string of Lastname, Firstname, uses the names function
    from billy to make a tuple and then rearranges it.'''  
    first_last = split_name(name)
    if first_last is not None:
        firstname, lastname = first_last
        return lastname + ", " + firstname
    else:
        return name

def flip_keep(frame, col = 'Col1'):
    names = []
    for data in frame[col]:
        data = str(data)
        comma = data.count(',')
        if comma == 1:
            names.append(data)
        elif comma == 0:
            data = flip_name(data)
            names.append(data)
        else:
                names.append(data)
    frame['Name'] = names
    return frame

Residents = pd.read_csv(Residents_path, index_col=False, names = cols)

Residents = addyear(Residents, col="Years in")
Residents = addphd(Residents)
Residents = getname(Residents)
Residents['Current_location'] = unstack3(Residents['Col2'])
Residents = Residents.dropna(thresh=6)
Residents = Residents[['Name','GRAD_YEAR','PhD','APCP','Med School','Current_location']]
Residents = flip_keep(Residents, col = 'Name')
Residents.to_csv(Fixed_path)