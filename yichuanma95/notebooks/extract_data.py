import pandas as pd

def extract_data(start_row, end_row, start_year=2005, end_year=2019):
    end_row += 1
    dfs = [generate_subdf(year, start_row, end_row) for year in range(start_year,
        end_year+1)]
    df = pd.concat(dfs)
    df.drop(columns=['Unnamed: 49', 'Unnamed: 50', 'Unnamed: 51',
        'Unnamed: 52'], inplace=True)
    df.fillna(0, inplace=True)
    return df

def generate_subdf(year, start, end):
    dfYear = pd.read_excel('../../data/Brazilian Immigrants.xlsx',
            sheet_name=str(year))
    subDf = dfYear[start:end]
    subDf = subDf.rename(columns={'Unnamed: 0': 'Type', 'State_Code': 'Type',
            'State_Code.1': 'State Code'}, errors='ignore')
    cols = subDf.columns.tolist()
    cols.insert(0, 'Year')
    subDf = subDf.reindex(columns=cols)
    years = [year] * (end - start)
    subDf['Year'] = years
    return subDf
