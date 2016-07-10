import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load Data
def load_data():
    census = pd.read_excel('data/SantaClaraCountyHomelessCensus.xlsx',
                           sheetname=0)
    return census

def load_variables():
    variable_labels = pd.read_excel('data/SantaClaraCountyHomelessCensus.xlsx',
                                    sheetname=1, skiprows=3)
    variable_labels.ix[variable_labels['LABEL'] == '<ninguno>', 'LABEL'] = \
        variable_labels.ix[variable_labels['LABEL'] == '<ninguno>', 'Variable']
    variable_labels.columns = ['Variable', 'Label', 'New Label']
    return variable_labels

def load_values():
    value_labels = pd.read_excel('data/SantaClaraCountyHomelessCensus.xlsx',
                                 sheetname=2, skiprows=2, skipfooter=1)
    value_labels = value_labels.ix[:, 1:]
    value_labels.columns = ['Variable', 'Value', 'Label']
    value_labels['Variable'] = value_labels['Variable'].fillna(method='ffill')
    return value_labels

def fill_NAs(census):
    # Fill NAs with 0s
    for col in census.columns[7:]:
        census[col] = census[col].fillna(0)
        census[col] = census[col].astype(int)
    return census

def replace_answers(census, variables, values):
    # Replace Data Cells with Intelligible Strings
    for ix, row in values[25:].iterrows():
        val = int(float(row['Value']))
        var = row['Variable']
        lab = row['Label']
        census[var] = census[var].replace(val, lab)
    return census

def replace_columns(census, variables, values):
    census.columns = variables['New Label'].values
    return census

if __name__ == '__main__':
    census, variables, values = load_data(), load_variables(), load_values()
    census = fill_NAs(census)
    census = replace_answers(census, variables, values)
    census = replace_columns(census, variables, values)
    census.to_csv('data/scch_census_ints.csv', index=False)
