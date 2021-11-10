import pandas as pd

def extract_data(start, end):
    end += 1
    dfs = []
    for year in range(2012, 2019+1):
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
        dfs.append(subDf)
    df = pd.concat(dfs)
    df.drop(columns=['Unnamed: 49', 'Unnamed: 50', 'Unnamed: 51',
        'Unnamed: 52'], inplace=True)
    df.fillna(0, inplace=True)
    return df
