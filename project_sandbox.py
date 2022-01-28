import csv
import pandas as pd
import numpy as np
import plotly.express as px


# this reads the csv file, and creates a list
# of the data called data_list


def read_csvfile(filename: str) -> list:
    """
    """
    data = []
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            data.append(line)

    return data


data_list = read_csvfile('ClimateandinfectiousdiseaseCSV3.csv')
ans_dict = {}
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
years = ['2007', '2008', '2009', '2010', '2011']

# this code creates a dictionary
# representing a month and a year,
# and how many cases were recorded then.
for month in months:
    for year in years:
        for indiv in data_list:
            if indiv[3] == month and indiv[5] == year:
                if f'{month}, {year}' not in ans_dict:
                    ans_dict[f'{month}, {year}'] = 1
                else:
                    ans_dict[f'{month}, {year}'] += 1

# we are creating this columns_data dictionary to be used in creating a data frame,
# which would go on to be plotted in a scatter plot.

columns_data = {'months': [], 'years': [], 'cases': []}

for month_year in ans_dict:
    columns_data['months'].append(month_year.split(',')[0])

    columns_data['years'].append(month_year.split(',')[1])

    columns_data['cases'].append(ans_dict[month_year])
# create a data frame df

df = pd.DataFrame(columns_data, columns=['months', 'years', 'cases'])

# this code create a line plot of the data frame df
fig = px.line(df, x='years', y='cases', color='months')

fig.show()

total_cases_dict = {}

for year in years:
    for indiv in data_list:
        if indiv[5] == year:
            if year in total_cases_dict:
                total_cases_dict[year] += 1
            else:
                total_cases_dict[year] = 1

columns_data_total = {'year': [], 'cases': []}

for year in total_cases_dict:
    columns_data_total['year'].append(year)
    columns_data_total['cases'].append(total_cases_dict[year])

df_total = pd.DataFrame(columns_data_total, columns=['years', 'cases'])

df_total.plot(x='years', y='cases', kind='bar')
# the following lines of code do the same thing for different age groups.

ans_dict_age_young = {}

for month in months:
    for year in years:
        for indiv in data_list:
            if int(indiv[1]) <= 18:
                if indiv[3] == month and indiv[5] == year:
                    if f'{month}, {year}' not in ans_dict_age_young:
                        ans_dict_age_young[f'{month}, {year}'] = 1
                    else:
                        ans_dict_age_young[f'{month}, {year}'] += 1

columns_data_age_young = {'months': [], 'years': [], 'cases': []}

for month_year in ans_dict_age_young:
    columns_data_age_young['months'].append(month_year.split(',')[0])

    columns_data_age_young['years'].append(month_year.split(',')[1])

    columns_data_age_young['cases'].append(ans_dict_age_young[month_year])

df_age_young = pd.DataFrame(columns_data_age_young, columns=['months', 'years', 'cases'])

fig_young = px.line(df_age_young, x='years', y='cases', color='months')

fig_young.show()

ans_dict_age_youth = {}

for month in months:
    for year in years:
        for indiv in data_list:
            if 18 < int(indiv[1]) <= 35:
                if indiv[3] == month and indiv[5] == year:
                    if f'{month}, {year}' not in ans_dict_age_youth:
                        ans_dict_age_youth[f'{month}, {year}'] = 1
                    else:
                        ans_dict_age_youth[f'{month}, {year}'] += 1

columns_data_age_youth = {'months': [], 'years': [], 'cases': []}

for month_year in ans_dict_age_youth:
    columns_data_age_youth['months'].append(month_year.split(',')[0])

    columns_data_age_youth['years'].append(month_year.split(',')[1])

    columns_data_age_youth['cases'].append(ans_dict_age_youth[month_year])

df_age_youth = pd.DataFrame(columns_data_age_youth, columns=['months', 'years', 'cases'])

fig_youth = px.line(df_age_youth, x='years', y='cases', color='months')

fig_youth.show()

ans_dict_age_middle = {}

for month in months:
    for year in years:
        for indiv in data_list:
            if 35 < int(indiv[1]) <= 55:
                if indiv[3] == month and indiv[5] == year:
                    if f'{month}, {year}' not in ans_dict_age_middle:
                        ans_dict_age_middle[f'{month}, {year}'] = 1
                    else:
                        ans_dict_age_middle[f'{month}, {year}'] += 1

columns_data_age_middle = {'months': [], 'years': [], 'cases': []}

for month_year in ans_dict_age_youth:
    columns_data_age_middle['months'].append(month_year.split(',')[0])

    columns_data_age_middle['years'].append(month_year.split(',')[1])

    columns_data_age_middle['cases'].append(ans_dict_age_middle[month_year])

df_age_middle = pd.DataFrame(columns_data_age_middle, columns=['months', 'years', 'cases'])

fig_middle = px.line(df_age_middle, x='years', y='cases', color='months')

fig_middle.show()

ans_dict_age_elder = {}

for month in months:
    for year in years:
        for indiv in data_list:
            if int(indiv[1]) > 55:
                if indiv[3] == month and indiv[5] == year:
                    if f'{month}, {year}' not in ans_dict_age_elder:
                        ans_dict_age_elder[f'{month}, {year}'] = 1
                    else:
                        ans_dict_age_elder[f'{month}, {year}'] += 1

columns_data_age_elder = {'months': [], 'years': [], 'cases': []}

for month_year in ans_dict_age_elder:
    columns_data_age_elder['months'].append(month_year.split(',')[0])

    columns_data_age_elder['years'].append(month_year.split(',')[1])

    columns_data_age_elder['cases'].append(ans_dict_age_elder[month_year])

df_age_elder = pd.DataFrame(columns_data_age_elder, columns=['months', 'years', 'cases'])

fig_elder = px.line(df_age_elder, x='years', y='cases', color='months')

fig_elder.show()



new_list = []
year = 2007
for indiv in data_list:
    if int(indiv[5]) == year:
        new_list.append(indiv)
        year += 1

temperature_dict = {'years': [], 'temperatures':[], 'months': [] }
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
