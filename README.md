# Qingyang Xu

# U86636173

# Running DataExtraction.ipynb

this file generates Median Personal Earnings and Employment by Occupation csv files 2005-2019.

function addYear(df,year,num):

df is the datatable, year is the year you want to extract, num is the number of rows you want to extract

i.e addYear(mpe_2005,2005,2): add one column 'Year' in table mpe_2005 and add two '2005'



# Running DataAnalysis.ipynb

this file do some basic analysis for single features

function plotmpe(statecode):

statecode is a list of state codes, and the function will generate line graphs of median personal earnings through years for each state

i.e plotmpe([25]) generates graph for MA

function eoForState(statecode):

statecode is a list of state codes, and the function will generate stacked bar graphs of employment by occupation through years for each state

i.e eoForState([25]) generates graph for MA


# Running PredictionModel.ipynb

this file does feature engineering and model training work to find correlation between features

y-median personal earnings per year

x1-percentage of people whose English skill is less proficient

x2-percentage of citizenship

x4-percentage of people entrying after 2000s

x5-labored female

x6-labored male

x7-unemployed female

x8-unemployed male

fe-female employment rate

me-male employment rate

g/d-employment rate

x9-percentage of people above poverty

x10-percentage of people in services industry amony all occupations

x11-percentage of people in healthcare and technique industry amony all occupations


All data is in data folder.
