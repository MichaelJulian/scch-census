import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import datetime
from explore import load_csv, plot_subset
from scipy.stats import pearsonr

def title(category):
    category = category.replace(':', '')
    dic = {'Reason': 'Reasons for Homelessness',
           'Housing Obstacle': 'Reported Housing Obstacles',
           'Job Obstacle': 'Reported Job Obstacles',
           'Government': 'Government Assistance Received',
           'No Assistance': 'Reasons for not Receiving Assistance',
           'Ethnicity': 'Ethnicity'}
    if category not in dic:
        title = 'Homeless Statistics'
    else:
        title = dic[category]
    return title

def heatmap(df, category1, category2, prob=True, cat1_sort=1):
    cols1 = df.columns[df.columns.str.contains(category1)][::cat1_sort]
    cols2 = df.columns[df.columns.str.contains(category2)]
    mat = []
    if prob:
        for col1 in cols1:
            row = [pd.crosstab(df[col1], df[col2]).apply(lambda r: r / r.sum(),
                                                      axis=1) for col2 in cols2]
            mat.append([xtab[1][1] for xtab in row])
    else:
        for col1 in cols1:
            row = [pd.crosstab(df[col1], df[col2]) for col2 in cols2]
            mat.append([xtab[1][1] for xtab in row])

    ax = sns.heatmap(mat)
    cols2 = [col.replace(category2, '').replace(':', '') for col in cols2]
    cols1 = [col.replace(category1, '').replace(':', '') for col in cols1]
    plt.xticks(np.arange(len(cols2))+.5, cols2, rotation=30)
    plt.yticks(np.arange(len(cols1))+.5, cols1[::-1], rotation=0)
    plt.title(title(category1) + ' (y-axis) versus ' + title(category2) + ' (x-axis)\n')
    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
    plt.show()
