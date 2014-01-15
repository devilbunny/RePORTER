#Make data frames from .csvs and does basic trim, and adds years to grant
import pandas as pd
import numpy as np
import datetime



RePORTER_path = 'C:\Users\JAG\RePORTER\Output\RePORT_Append.csv'
Residents_path = 'C:\Users\JAG\RePORTER\Residencies\perimatch-fixb.csv'
Residents_With_Grants_path = "C:\Users\JAG\RePORTER\Residencies\perimatch-RWGb.csv"

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
        newname = names[0] + ", " + names[1][1:4]
        return newname
    except IndexError:
        return name

def years_to_grant(frame, GRAD_YEAR_col = 'GRAD_YEAR', 
                    BUDGET_START_col = 'BUDGET_START'):
    ''' *frame*, *GRAD_YEAR_col* = 'GRAD_YEAR', *BUDGET_START_col* =
    'BUDGET_START',
    Generates a column showing the time between graduation and the 
    budget start of a grant in months'''
    GRAD_YEAR = []

    for date in frame[GRAD_YEAR_col]:
        date = str(date)
        date = '7/1/' + date
        GRAD_YEAR.append(date)
    
    frame['GY_date'] = pd.to_datetime(GRAD_YEAR, coerce = True)
    frame['BS_date'] = pd.to_datetime(frame[BUDGET_START_col], coerce = True)

    frame['Years_to_grant'] = frame['BS_date'] - frame['GY_date']
    frame['Years_to_grant'] = [data.astype(float) for data in frame['Years_to_grant']]
    frame['Years_to_grant'] = frame['Years_to_grant'] / 3.15576e+16
    
    return frame


Residents = pd.read_csv(Residents_path, index_col=False, header=0, squeeze=True)
RePORTER = pd.read_csv(RePORTER_path, index_col=False, header=0, squeeze=True)

simple_names = [simple_name(name).upper() if isinstance(name, basestring) else name for name in Residents['Name']]
Residents['Simple_names'] = simple_names
simple_names = [simple_name(name).upper() if isinstance(name, basestring) else name for name in RePORTER['PI_NAMEs']]
RePORTER['Simple_names'] = simple_names

Residents_With_Grants = Residents.merge(RePORTER)
Residents_With_Grants = years_to_grant(Residents_With_Grants, GRAD_YEAR_col = 'GRAD_YEAR')
Residents_With_Grants.to_csv(Residents_With_Grants_path, sep = ',' , index = False)
