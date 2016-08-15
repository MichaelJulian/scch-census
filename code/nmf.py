import pandas as pd
import numpy as np
from sklearn.decomposition import NMF
import matplotlib.pyplot as plt
from explore import load_csv

def fit_nmf(k):
    nmf = NMF(n_components=k)
    nmf.fit(M)
    W = nmf.transform(M)
    H = nmf.components_
    return nmf.reconstruction_err_


if __name__ == '__main__':
    df = load_csv()
    df['Male'] = (df.Gender=='Male').astype(int)
    reas = df.columns[df.columns.str.contains('Reason:')]
    prev = df.columns[df.columns.str.contains('Prevention:')]
    obs = df.columns[df.columns.str.contains('Obstacle:')]

    M = df[reas + prev + obs + ['Male']]

    error = [fit_nmf(i) for i in range(1, 12)]
    plt.plot(range(1, 12), error)
    plt.xlabel('k')
    plt.ylabel('Reconstruction Errror')


    num_reasons = []
    for i, row in df.iterrows():
        num_reasons.append(row[reas].sum())
    df['num_reasons'] = num_reasons

    num_prev = []
    for i, row in df.iterrows():
        num_prev.append(row[prev].sum())
    df['num_prevention'] = num_prev

    num_obstacles = []
    for i, row in df.iterrows():
        num_obstacles.append(row[obs].sum())
    df['num_obstacles'] = num_obstacles
