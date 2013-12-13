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
    for data in frame['Col1']:
        try:
            data = int(data)
            year = data
            GRAD_YEAR.append(data)
        except ValueError:
            GRAD_YEAR.append(year)

    frame['GRAD_YEAR'] = GRAD_YEAR
    return frame
    #csvs = [path for path in paths if path[-3:] == "csv"]
    #reversed_names = [flip_name(name).upper()+';' if isinstance(name, basestring) else name for name in Residents['PI_NAMEs']]

        

