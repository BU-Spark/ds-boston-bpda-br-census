How to Run Code:
1. use jupyter notebook or google collab
2. depending on selected place to run the notebooks, import data files (in data folder) to the same directory/path as the notebook you are running (or update imports accordingly)
3. the code produces the results right below the cell

- There are certain main functions that were used for repetitive data anaylsis:
    - getFeatureData --> given an index in the data returns a list over all the years and all states for that data point index
    - makeFeatureDataListState --> given the data, list of years, index, and state code, returns a list of data points over the years for that given state
    - makeCorrGraph --> makes a confusion matrix when given a dataframe, list of column names (to be displayed), and the title of the confusion matrix
    - makeLinReg --> given two dataframes, X is independent variables and y is dependent variable, performs linear regression using stats model OLS package 
    - Not a function but in cells 2, 3, 4 up from the bottom uses sklearn library and makes a graph of the linear regression