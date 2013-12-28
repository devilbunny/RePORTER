# Generates plots
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


Residents_plus_grants_path = "C:\Users\JAG\RePORTER\Residencies\perimatch-G3.csv"
Figure_path = 'C:\Users\JAG\RePORTER\Figures\\'

RWG_fix = pd.read_csv(Residents_plus_grants_path, sep=',' , index_col = False, header =0)
RWG_fix['Any_grant'] = RWG_fix['TOTAL_COST'] > 0

'''
# This is for the perimatch scatter plots
fig = plt.figure()
plt.scatter((RWG_fix.Prematch + RWG_fix.Perimatch), RWG_fix.TOTAL_COST)
plt.savefig(Figure_path + 'preperimatch_vs_grantmoney_scatter.png')

fig = plt.figure()
plt.scatter((RWG_fix.Prematch), RWG_fix.TOTAL_COST)
plt.savefig(Figure_path + 'prematch_vs_grantmoney_scatter.png')

fig = plt.figure()
plt.scatter((RWG_fix.Perimatch), RWG_fix.TOTAL_COST)
plt.savefig(Figure_path + 'perimatch_vs_grantmoney_scatter.png')

fig = plt.figure()
plt.scatter((RWG_fix.Postmatch), RWG_fix.TOTAL_COST)
plt.savefig(Figure_path + 'postmatch_vs_grantmoney_scatter.png')

fig = plt.figure()
plt.scatter((RWG_fix.Prematch + RWG_fix.Perimatch), RWG_fix.Postmatch)
plt.savefig(Figure_path + 'pre_vs_postmatch_scatter.png')

# This is a bar chart showing K08s by year
RWG_groupped = RWG_fix.groupby('GRAD_YEAR').count()
RWG_pct = RWG_groupped.K08.astype(float) / RWG_groupped.Name.astype(float) * 100
print RWG_pct
fig = plt.figure()
RWG_pct.plot(kind = 'bar')
plt.savefig(Figure_path + 'perimatch_bar.png')


TOTAL_COST = RWG_fix['TOTAL_COST']
logTC = TOTAL_COST
#logTC = np.log10(logTC)
logTC = logTC[0:17]
Preperimatch = RWG_fix['Prematch'] + RWG_fix['Perimatch']
line = []
array = []

line = stats.linregress(Preperimatch[0:17], logTC)
array.append(line)

line = stats.linregress(RWG_fix['Prematch'][0:17], logTC)
array.append(line)

line = stats.linregress(RWG_fix['Perimatch'][0:17], logTC)
array.append(line)

line = stats.linregress(RWG_fix['Postmatch'][0:17], logTC)
array.append(line)

line = stats.linregress(Preperimatch, RWG_fix['Postmatch'])
array.append(line)


Regressions = pd.DataFrame(array, index = ['Preperimatch vs $', 'Prematch vs $', 'Perimatch vs $',
'Postmatch vs $', 'Preperimatch vs. Postmatch'], columns = ['Slope', 'Intercept', 'r_value','p_value','std_error'])
print Regressions
Regressions.to_csv(Figure_path + 'Perimatch_Regressions.csv', sep = ',')


# This is a cross-tab showing grants by specialty
Cross = pd.crosstab(RWG_fix.Fix_Spec, RWG_fix.Any_grant, margins = True)
print Cross
Cross.to_csv(Figure_path + 'Perimatch_grants_by_specialty.csv', sep = ',')

# This is a cross-tab showing grants by traditional fellowship or not
Cross = pd.crosstab(RWG_fix.Traditional_fellowship, RWG_fix.Any_grant, margins = True)
print Cross
Cross.to_csv(Figure_path + 'Perimatch_grants_by_traditional.csv', sep = ',')
'''

# This is a histogram of papers published vs probability of later grants
bins = np.array([-1, 0, 1, 2, 3, 4, 5, 6, 100])

RWG_grant = RWG_fix[RWG_fix['Any_grant'] == True]
count = RWG_grant.Name.count()
print count
labels = pd.cut(RWG_grant.Prematch, bins)
RWG_grant = RWG_grant.groupby(labels).count()
RWG_pct = (RWG_grant.Name.astype(float) / count.astype(float)) * 100
print RWG_pct
fig = plt.figure()
RWG_pct.plot(kind = 'bar')
plt.savefig(Figure_path + 'grant_paper_pct.png')

RWG_nogrant = RWG_fix[RWG_fix['Any_grant'] == False]
count = RWG_nogrant.Name.count()
print count
labels = pd.cut(RWG_nogrant.Prematch, bins)
RWG_nogrant = RWG_nogrant.groupby(labels).count()
RWG_pct = (RWG_nogrant.Name.astype(float) / count.astype(float)) * 100
print RWG_pct
fig = plt.figure()
RWG_pct.plot(kind = 'bar')
plt.savefig(Figure_path + 'nogrant_paper_pct.png')
'''
RWG_groupped = RWG_fix.groupby('GRAD_YEAR').count()
RWG_pct = RWG_groupped.K08.astype(float) / RWG_groupped.Name.astype(float) * 100
'''