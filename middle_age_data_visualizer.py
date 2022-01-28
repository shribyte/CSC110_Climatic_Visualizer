from total_data_visualizer import *


def create_dictionary(months: List, years: List) -> dict:
    """
    Create a dictionary
    representing a month and a year,
    and how many cases were recorded then
    (only concerned with the younger population).
    """
    data_list = read_csvfile('ClimateandinfectiousdiseaseCSV3.csv')
    ans_dict = {}
    for month in months:
        for year in years:
            for indiv in data_list:
                if 35 < int(indiv[1]) <= 55:
                    if indiv[3] == month and indiv[5] == year:
                        if f'{month}, {year}' not in ans_dict:
                            ans_dict[f'{month}, {year}'] = 1
                        else:
                            ans_dict[f'{month}, {year}'] += 1
    return ans_dict


def visualize_middle() -> None:
    """
    Visualize the data only concerning the young population.
    Note: This function shadows the function from the import statement.
    """
    ans_dict = create_dictionary(months=['January', 'February', 'March', 'April', 'May', 'June',
                                         'July', 'August', 'September',
                                         'October', 'November', 'December'],
                                 years=['2007', '2008', '2009', '2010', '2011'])
    columns_data = columns_data_creater(ans_dict)
    df = create_dataframe(columns_data)
    fig = px.line(df, x='years', y='cases', color='months')
    fig.show()


if __name__ == '__main__':
    visualize_middle()
    # python_ta.check_all(config={
    #  'extra-imports': ['total_data_visualizer'],
    # the names (strs) of imported modules
    #    'allowed-io': [],  # the names (strs) of functions that call print/open/input
    #   'max-line-length': 100,
    #    'disable': ['R1705', 'C0200']
    # })
