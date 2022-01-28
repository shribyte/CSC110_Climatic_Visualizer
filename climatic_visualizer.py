from total_data_visualizer import *



def list_helper(data_list: list):
    new_list = []
    year = 2007
    for indiv in data_list:
        if int(indiv[5]) == year:
            new_list.append(indiv)
            year += 1
    return new_list


def visualize_temperature(new_list: list):
    temperature_dict = {'years': [], 'temperatures': [], 'months': []}
    year = 2007
    for indiv in new_list:
        i = 6
        for month in months:
            temperature_dict['months'].append(month)
            temperature_dict['years'].append(year)
            temperature_dict['temperatures'].append(indiv[i])
            i += 1
        year += 1
    temperature_df = pd.DataFrame(temperature_dict, columns=['years', 'temperatures', 'months'])

    fig = px.line(temperature_df, x='years', y='temperatures', color='months')
    fig.show()


def visualize_humidity(new_list: list):
    humidity_dict = {'years': [], 'humidities': [], 'months': []}
    year = 2007
    for indiv in new_list:
        i = 18
        for month in months:
            humidity_dict['months'].append(month)
            humidity_dict['years'].append(year)
            humidity_dict['humidities'].append(indiv[i])
            i += 1
        year += 1

    humidity_df = pd.DataFrame(humidity_dict, columns=['years', 'humidities', 'months'])

    fig = px.line(humidity_df, x='years', y='humidities', color='months')
    fig.show()


def visualize_precipitation(new_list: list):
    precip_dict = {'years': [], 'precip': [], 'months': []}

    year = 2007
    for indiv in new_list:
        i = 30
        for month in months:
            precip_dict['months'].append(month)
            precip_dict['years'].append(year)
            precip_dict['precip'].append(indiv[i])
            i += 1
        year += 1

    precip_df = pd.DataFrame(precip_dict, columns=['years', 'precip', 'months'])

    fig = px.line(precip_df, x='years', y='precip', color='months')
    fig.show()


if __name__ == '__main__':
    data_list = read_csvfile('ClimateandinfectiousdiseaseCSV3.csv')
    new_list = list_helper(data_list)
    visualize_temperature(new_list)
    visualize_humidity(new_list)
    visualize_precipitation(new_list)

    # python_ta.check_all(config={
    #  'extra-imports': ['total_data_visualizer'],
    # the names (strs) of imported modules
    #    'allowed-io': [],  # the names (strs) of functions that call print/open/input
    #   'max-line-length': 100,
    #    'disable': ['R1705', 'C0200']
    # })
