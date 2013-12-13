#Make data frames from .csvs and does basic trim
import pandas as pd
import numpy as np
import datetime



RePORTER_path = 'C:\Users\JAG\RePORTER\Output\RePORT_Append.csv'
Residents_path = 'C:\Users\JAG\RePORTER\Residencies\perimatch-fix.csv'
Residents_With_Grants_path = "C:\Users\JAG\RePORTER\Residencies\perimatch-RWG.csv"

def flip_name(name):
    ''' takes a string in the format of Firstname Lastname and returns a string of Lastname, Firstname, uses the names function
    from billy to make a tuple and then rearranges it.'''  
    first_last = split_name(name)
    if first_last is not None:
        firstname, lastname = first_last
        return lastname + ", " + firstname
    else:
        return name

def simple_name(name):
    ''' takes a string of the format Lastname, Firstname stuf stuf stuff
    and returns a string of the format Lastname, Fir'''
    names = name.split(",")
    try:
        return names[0] + ", " + names[1][1:4]
    except IndexError:
        return name

def years_to_grant(frame, GRAD_YEAR_col = 'GRAD_YEAR', 
                    BUDGET_START_col = 'BUDGET_START'):
    ''' *frame*, *GRAD_YEAR_col* = 'GRAD_YEAR', *BUDGET_START_col* =
    'BUDGET_START',
    Generates a column showing the time between graduation and the 
    budget start of a grant in months'''
    GRAD_YEAR = []
    BUDGET_START = []
    YEARS_TO_GRANT = []
    
    for date in frame[GRAD_YEAR_col]:
        date = int(date)
        GRAD_YEAR.append(date)
    
    for date in frame[BUDGET_START_col]:
        try:
            date = date[-4:]
            date = int(date)
        except TypeError:
            date = None
        BUDGET_START.append(date)   
    frame['Temp1'] = GRAD_YEAR
    frame['Temp2'] = BUDGET_START
    frame['Years_to_grant'] = frame['Temp2'] - frame['Temp1']
    frame = frame.drop('Temp1', 1)
    frame = frame.drop('Temp2', 1)

    return frame

Residents = pd.read_csv(Residents_path, index_col=False, header=0, squeeze=True)
RePORTER = pd.read_csv(RePORTER_path, index_col=False, header=0, squeeze=True)

simple_names = [simple_name(name).upper() if isinstance(name, basestring) else name for name in Residents['Name']]
Residents['Simple_names'] = simple_names
simple_names = [simple_name(name).upper() if isinstance(name, basestring) else name for name in RePORTER['PI_NAMEs']]
RePORTER['Simple_names'] = simple_names

Residents_With_Grants = Residents.merge(RePORTER)
Residents_With_Grants = years_to_grant(Residents_With_Grants, GRAD_YEAR_col = 'Year beginning fellowship')
Residents_With_Grants = Residents_With_Grants[Residents_With_Grants.Years_to_grant >= 0]
Residents_With_Grants.to_csv(Residents_With_Grants_path, sep = ',' , index = False)
