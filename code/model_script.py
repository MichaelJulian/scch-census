import pandas as pd
from explore import load_csv
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import train_test_split

def cols_that_contain(key):
    return df.columns[df.columns.str.contains(key)]

def predict_mental():
    df = load_csv()
    target_col = 'Health: Psychiatric Condition'
    train_cols = ['Obstacle', 'Sexuality', 'Ethnicity', 'Prevention', 'Male']
    df['Male'] = (df['Gender'] == 'Male').astype(int)
    cols = []
    for col in train_cols:
        cols.extend(cols_that_contain(col))

    target = (df[target_col] == 'Yes').astype(int)
    data = df[cols]

    tree = DecisionTreeClassifier(max_depth=2)
    tree.fit(data, target)
    data.columns[tree.tree_.feature]

    X_train, X_test, y_train, y_test = train_test_split(data, target)


if __name__ == '__main__':
    df = load_csv()
    target_col = 'Domestic Abuse (Current)'
    train_cols = ['Obstacle', 'Sexuality', 'Government',
                  'Reason', 'Prevention']

    cols = []
    for col in train_cols:
        cols.extend(cols_that_contain(col))

    target = (df[target_col] == 'Yes').astype(int)
    data = df[cols]

    tree = DecisionTreeClassifier(max_depth=2)
    tree.fit(data, target)
    data.columns[tree.tree_.feature]

    X_train, X_test, y_train, y_test = train_test_split(data, target)
