import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
def load_data():
    census = pd.read_excel('data/SantaClaraCountyHomelessCensus.xlsx', sheetname=0)
    return census

def load_variables():
    variable_labels = pd.read_excel('data/SantaClaraCountyHomelessCensus.xlsx', sheetname=1, skiprows=3)
    variable_labels.ix[variable_labels['LABEL'] == '<ninguno>', 'LABEL'] = variable_labels.ix[variable_labels['LABEL'] == '<ninguno>', 'Variable']
    variable_labels.columns = ['Variable', 'Label']
    return variable_labels

def load_values():
    value_labels = pd.read_excel('data/SantaClaraCountyHomelessCensus.xlsx', sheetname=2, skiprows=2, skipfooter=1)
    value_labels = value_labels.ix[:, 1:]
    value_labels.columns = ['Variable', 'Value', 'Label']
    for ix, variable in enumerate(value_labels['Variable']):
        if type(variable) != float:
            variable_name = variable
        else:
            value_labels['Variable'][ix] = variable_name
    return value_labels

def clean_data(census, variables, values):
    for ix, row in values.iterrows():
        val = row['Value']
        var = row['Variable']
        lab = row['Label']
        census.ix[census[var].astype(int).astype(str) == val, var] = lab
