'''The purpose of this script is to take a directory of individual ExPORTER (RePORTER 
data in .csv form) files, either as .zip or as .csv, and make a new .csv
that contains a subset of the columns from each file, concatennated
in this version, I am including titles, and restricting the grant types to graduate F and K types'''
import pandas as pd
import zipfile
import os


input_path = 'C:\Users\JAG\RePORTER\Data\\'
output_path = 'C:\Users\JAG\RePORTER\Output\\RePORT_Append_Titles.csv'

def unziphere (paths, inputdir = os.getcwd(), target=os.getcwd()):
    '''*[paths]* list of target files, target='\Unzipped\\' unzips a list of files to the target directory'''
    os.chdir(inputdir)
    paths2 = [path for path in paths if path[-3:] == "zip"]
    for path in paths2:
        z = zipfile.ZipFile(path)
        z.extractall(target)

def GetRePORT (path, cols=['APPLICATION_ID', 'ACTIVITY', 'PI_NAMEs', 'ORG_NAME', 'ORG_CITY', 'BUDGET_START', 'PROJECT_TITLE', 'TOTAL_COST']):
    # path of csv to be read, cols = default set of columns, returns dataframe based on *path* with *cols*
    frame = pd.read_csv(path, index_col=False, header=0, squeeze=True)
    trim_frame = frame[cols]
    return trim_frame

def RePORT_Append (directory = os.getcwd(), target=os.getcwd() + 'RePORTER_Append.csv'):
    paths = os.listdir(directory)
    zips = [path for path in paths if path[-3:] == "zip"]
    unziphere(zips, inputdir = directory, target = directory)
    paths = os.listdir(directory)
    csvs = [path for path in paths if path[-3:] == "csv"]
    for path in csvs:
        frame = GetRePORT(directory + path)
        frame = restrict_types(frame, ['F32','K01','K08','K12','K23','K24','K99'], mode = 'a')
        frame.to_csv(target, sep = ',' , index = False, mode = 'a')
    return



def restrict_types (frame, types, mode='a'):
    if mode == 'a':
        frame = restrict_types_sub(frame, types)
        return frame
    elif mode == 'pre':
        framePRE = frame[frame.Years_to_grant < 0]
        framePOST = frame[frame.Years_to_grant >= 0]
        framePRE = restrict_types_sub(framePRE, types)
        frame = pd.concat([framePRE, framePOST])
        return frame
    elif mode == 'post':
        framePRE = frame[frame.Years_to_grant < 0]
        framePOST = frame[frame.Years_to_grant >= 0]
        framePOST = restrict_types_sub(framePOST, types)
        frame = pd.concat([framePRE, framePOST])
        return frame
    else:
        return frame
        
def restrict_types_sub (frame, types):
    pieces = []
    for activity in types:
        activityframe = frame[frame.ACTIVITY == activity]
        pieces.append(activityframe)
    restrictedframe = pd.concat(pieces)
    return restrictedframe


RePORT_Append(directory = input_path, target = output_path)

'''
# years = years for which compiled data are available
# weeks are for 2012 - 2014 where only week-by-week data are available
years = range (2006,2013)
week_years = range(2013,2016)
week_numbers = range(69,140)

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