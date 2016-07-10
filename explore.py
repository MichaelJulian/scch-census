import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import datetime

def load_csv():
    df = pd.read_csv("data/scch_census_ints.csv", parse_dates=[6])

    ages = (datetime.date.today() - df['Date of Birth'])
    df['age'] = ages / np.timedelta64(1, 'Y')

    return df

def convert_int(df, column):
    return df[df[column] != 'No Answer'][column].astype(float)

def search_cols(df, keyword):
    return df.columns[df.columns.str.contains(keyword)]

def plot_crosstab(df, col1, col2):
    xtab = pd.crosstab(df[col1], df[col2]).apply(lambda r: r / r.sum(), axis=1)
    sns.barplot(x=xtab.index, y=xtab.get_values()[:, 1])
    plt.ylabel('Probability of answering {}'.format(col2))
    plt.title('{} (x) vs Probability of {} (y)'.format(col1, col2))
    plt.show()

def terms():
    print 'Sexuality, Ethnicity, Household Member'
    print 'Reason, Housing Obstacle, Prevention'
    print 'Job Obstacle, Health, Domestic Abuse'
    print 'Services, Government, No Assistance, Jail'

'''
Display bar graph, where xticks are columns of a certain category,
ie Prevention: Transportation is an individual tick and category is Prevention.
All data is subsetted by a given column where values == 1.
'''

def plot_subset(df, subset, category, prob=True):
    cols = df.columns[df.columns.str.contains(category)]
    if prob:
        xtabs = [pd.crosstab(df[subset], df[col]).apply(lambda r: r / r.sum(),
                                                        axis=1) for col in cols]
    else:
        xtabs = [pd.crosstab(df[subset], df[col]) for col in cols]
    vals = [xtab.get_values()[1, 1] for xtab in xtabs]
    cols = [col.replace(category, '') for col in cols]
    ax = sns.barplot(cols, vals)
    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
    plt.show()

# def plot_subset(boolean, term):
#     subset =
#     pass

#
#
#
#
# xtab = pd.crosstab(rating_bins,
#             df['churn']).apply(lambda r: r/r.sum(), axis=1)
# sns.pointplot(x=xtab.index, y=xtab[1])
# plt.xlabel('Rating of Driver Intervals')
# plt.ylabel('Probability of Churn')
# plt.title('Probability of Churn based on Rating of Driver')
# plt.show()
#
#
# xtab = pd.crosstab(df['hasnt_rated'],
#             df['churn']).apply(lambda r: r/r.sum(), axis=1)
# sns.barplot(x=xtab.index, y=xtab[1])
# plt.xlabel("Has Rated Driver (Left) vs Hasn't (Right)")
# plt.ylabel("Probability")
# plt.title("Missing Rating of Driver vs Churn Rate")
# plt.show()
