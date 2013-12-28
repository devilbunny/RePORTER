#Guess PhD - uses google search to get hits for a person's name with and without
# PhD appended, then guesses whether they have a PhD
# based on the 'Google fight' program from Krumins

from xgoogle.search import GoogleSearch, SearchError
import numpy as np
import pandas as pd
import time

Residents_path = "C:\Users\JAG\RePORTER\Residencies\perimatch-G2.csv"
Residents_phd_path = "C:\Users\JAG\RePORTER\Residencies\perimatch-G2p.csv"

def phd_by_google (frame, col = 'Name', title='PhD'):
    #Takes a frame, and uses google to count the number of hits
    # for each Name in col with and without title (default PhD)
    # Theoretically, a PhD should get more hits?
    names = frame[col]
    wo_title = []
    w_title = []
    for name in names:
        wo_count = count_results(name)
        w_count = count_results(name + ' PhD')
        wo_title.append(wo_count)
        w_title.append(w_count)
        print name + ' ' + wo_count + ', w/PhD ' + w_count
    frame['wo_title'] = wo_title
    frame['w_title'] = w_title
    return frame

def count_results (term):
        try:
            gs = GoogleSearch(term) #a google search object for the term
            gs.results_per_page = 50
            res = []
            while True:
                tmp = gs.get_results()
                if not tmp:
                    break
                res.extend(tmp)
                time.sleep(2)
            gs_count = len(res)
            return gs_count
        except SearchError, e:
            print "Search failed: %s" % e
            return None




Residents = pd.read_csv(Residents_path, sep = ',' , index_col = False, header =0)
Residents = phd_by_google(Residents, col = 'Name', title = 'PhD')
Residents.to_csv(Residents_phd_path, sep = ',' , index = False)
