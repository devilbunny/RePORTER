'''Perimatch wrangle
To wrangle complicated files with year of graduation proceeding several names
Names are of format:
Last, First Degree(s) (ProgramType)", "New Job, Institution, City, State"
'''
import pandas as pd
import numpy as np
from names import split_name

def addyear (frame, years = (2000,2015), col="Col1"):
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


def dropMD (frame, col = 'Col1'):
     '''*DataFrame*, *column = 'Col1'* returns whatever string is before
     ', MD' in the string in column'''
     names = []
     for data in frame[col]:
         try:
            data = str(data)
            data2 = data.split(', MD')
            name = data2[0]
         except IndexError:
             name = None
         names.append(name)       
     frame[col] = names
     return frame

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

def YNTF (frame, col="Col1", newcol = ''):
    ''' 'Yes/No/True/False' - *frame*, *col* = 'Col1', *newcol* = ''
    converts a column of yesses and noes to True and False based
    on looking for y or n.  If a string is passed as newcol, the
    T/F will be put into a new column named newcol, if not, it 
    replaces the original'''
    TF = []
    for data in frame[col]:
        data = str(data)
        data = data.upper()
        if data.count('Y') == 1:
            TF.append(True)
        elif data.count('N') == 1:
            TF.append(False)
        else:
            TF.append(None)
    if newcol == '':
        frame[col] = TF
    else:
        frame[newcol] = TF
    return frame

def fix_specialty (frame, dictionary, col="Specialty", newcol = ''):
    ''' *frame*, *dictionary*, *col* = 'Specialty', *newcol* = '' 
    - converts a column of yesses and noes
    to True and False based on looking for y or n
    If a string is passed as newcol, the T/F will be put 
    into a new column named newcol, if not, it 
    replaces the original'''
    specialty = []
    for data in frame[col]:
        data = str(data)
        data = data.upper()
        if data.count('Y') == 1:
            TF.append(True)
        elif data.count('N') == 1:
            TF.append(False)
        else:
            TF.append(None)
    if newcol == '':
        frame[col] = TF
    else:
        frame[newcol] = TF
    return frame

Residents_path = 'C:\Users\JAG\RePORTER\Residencies\perimatch.csv'
Fixed_path = 'C:\Users\JAG\RePORTER\Residencies\perimatch-fix.csv'


Residents = pd.read_csv(Residents_path, index_col=False, header=0)
Residents = Residents.drop('Unnamed: 0' , 1)
Residents = Residents.drop('ID number',1)
Residents = dropMD(Residents, col='Name')
Residents = flip_keep(Residents, col = 'Name')
Residents = YNTF(Residents, col = 'Traditional fellowship')
Residents.to_csv(Fixed_path)
