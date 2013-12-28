#RWG wrangle takes a csv of residents with grants and does some operations
# 1. it strips out non F, K, or R grants
# at this point the remaining grants should be manually verified
# 2. it determines the earliest year when residents received a grant


import pandas as pd
import numpy as np

RWG_path = "C:\Users\JAG\RePORTER\Residencies\perimatch-RWG.csv"
RWG_fix_path = "C:\Users\JAG\RePORTER\Residencies\perimatch-RWG-f.csv"
Residents_path = "C:\Users\JAG\RePORTER\Residencies\perimatch-fix.csv"

pretypes = ['F30','F31']
posttypes = ['F32','K01','K08','K12','K23','K24','R01','R03','R15','R21','R43','R56']



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


RWG = pd.read_csv(RWG_path, index_col=False, header=0, squeeze=True)
RWG = restrict_types(RWG, pretypes, mode='pre')
RWG = restrict_types(RWG, posttypes, mode='post')
RWG.to_csv(RWG_fix_path, sep = ',' , index = False)