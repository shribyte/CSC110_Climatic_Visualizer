from data_loader import read_csvfile
import python_ta
from typing import List
import pandas as pd
import plotly.express as px

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
years = ['2007', '2008', '2009', '2010', '2011']


def create_dictionary(months: List, years: List) -> dict:
    """
    Create a dictionary
    representing a month and a year,
    and how many cases were recorded then.
    """
    data_list = read_csvfile('ClimateandinfectiousdiseaseCSV3.csv')
    ans_dict = {}
    for month in months:
        for year in years:
            for indiv in data_list:
                if indiv[3] == month and indiv[5] == year:
                    if f'{month}, {year}' not in ans_dict:
                        ans_dict[f'{month}, {year}'] = 1
                    else:
                        ans_dict[f'{month}, {year}'] += 1
    return ans_dict


def create_dataframe(columns_data: dict) -> pd.DataFrame:
    """
    Create a dateframe, using the given columns data dictionary.
    """
    return pd.DataFrame(columns_data, columns=['months', 'years', 'cases'])


def columns_data_creater(ans_dict: dict):
    """
    Using the output dictionary from create_dictionary, create
    another dictionary that can be used to generate a DataFrame object.
    """

    columns_data = {'months': [], 'years': [], 'cases': []}

    for month_year in ans_dict:
        columns_data['months'].append(month_year.split(',')[0])

        columns_data['years'].append(month_year.split(',')[1])

        columns_data['cases'].append(ans_dict[month_year])

    return columns_data


def visualize() -> None:
    ans_dict = create_dictionary(months=['January', 'February', 'March', 'April', 'May', 'June',
                                         'July', 'August', 'September',
                                         'October', 'November', 'December'],
                                 years=['2007', '2008', '2009', '2010', '2011'])
    columns_data = columns_data_creater(ans_dict)
    df = create_dataframe(columns_data)
    fig = px.line(df, x='years', y='cases', color='months')
    fig.show()


if __name__ == '__main__':
    visualize()
    # python_ta.check_all(config={
    #  'extra-imports': ['data_loader', 'python_ta', 'typing', 'pandas', 'plotly.express'],
    #    'allowed-io': [],  # the names (strs) of functions that call print/open/input
    #   'max-line-length': 100,
    #    'disable': ['R1705', 'C0200']
    # })
