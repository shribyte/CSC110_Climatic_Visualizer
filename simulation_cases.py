import random


# Assuming the baseline_temperatures to be the current average monthly temperatures in Sylhet, Bangladesh.
# Assuming the baseline_precipitation_level the current average precipitation levels in Sylhet, Bangladesh.

def mutate_temperature(baseline_temperature: float, month: int) -> float:
    """
    Mutate the temperature of the system, assuming events that cause temperature change.
    Note: The mutation is more in the summer months.

    Preconditions:
        - baseline_temperature in range(min(baseline_temperatures), max(baseline_temperatures))

    """

    if month in [3, 4, 5, 6, 7, 8]:
        baseline_temperature += random.randint(0, 200) / 10000
    else:
        baseline_temperature += random.randint(0, 100) / 10000

    return baseline_temperature


def mutate_precipitation_level(baseline_precipitation: float, month: int) -> float:
    """
    Mutate the precipitation level of the system (depending on the month). Assume events that cause this to be the case.
    Note: The mutation is more in the summer months.

    Preconditions:
        - baseline_precipitation in range(min(baseline_precipitations), max(baseline_precipitations))
    """
    if month in [3, 4, 5, 6, 7, 8]:
        baseline_precipitation += random.randint(0, 200) / 1000
    else:
        baseline_precipitation += random.randint(0, 100) / 1000
    return baseline_precipitation


def biting_rate(adult_mosquitoes: float) -> float:
    """
    Calculate the biting rate of a female Anopheles mosquito.
    Assuming that about 1-10 percent of the population of adult mosquitoes
    survive the inoculation period.

    Note: For the sake of precision, biting_rate can be a
    decimal number.

    Preconditions:
        - adult_mosquitoes >= 0

    """

    return random.uniform(0.01, 0.1) * adult_mosquitoes


def infection_rate(bites: float):
    """
    Return the number of bites that turn out to be infectious, and lead to
    malarial cases.
    Note: Assuming that 80 (err. 20) percent of the mosquito bites
    turn out to be infectious.
    """
    return (0.8 + random.uniform(-0.2, 0.2)) * bites


def adult_mosquito_abundance(larvae: float) -> float:
    """
    A relative measure of adult mosquito population old enough to potentially be capable of transmitting malaria.
    Note: It is assumed (statistic taken from study), that only 2.1 percent to 4.7 percent of the larvae
    mature into adult parasite-carrying mosquitoes.
    """

    return (random.uniform(0.021, 0.047)) * larvae


def mosquito_larvae_abundance(temperature: float, temperature_change: float, precipitation_change: float,
                              larvae: float):
    """
    Calculate the larvae population in the system
    given the increase in temperature,
    precipitation, and the current
    larval level in the system.

    Note: We assume that for unit increase in temperature, there is larval population increase.
    The increase depends on the temperature, and the corresponding current larval population,
    given in the list temperature_larvae.
    We also assume that the change reflected due to temperature_change in much more (about 3 times)
    that of the change reflected due to a precipitation_level change.

    Preconditions:
        - temperature >= 18
        - temperature_change >= 0
        - precipitation_change >= 0
        - larvae > 500

    """
    temperature_larvae = [650, 1100, 1500, 1750, 1850, 2000, 2100, 2250, 2250, 2150, 2050, 1950, 1750, 1500, 1250, 875,
                          250]
    cur_temp = temperature + temperature_change
    cur_temp_index = round(cur_temp) - 17
    if 18 <= cur_temp <= 20:
        larvae += (temperature_change * temperature_larvae[cur_temp_index]) + (precipitation_change *
                                                                               temperature_larvae[
                                                                                   cur_temp_index] * 0.03)
    elif 20 < cur_temp <= 23:
        larvae += ((temperature_change * temperature_larvae[cur_temp_index]) + (precipitation_change *
                                                                                temperature_larvae[
                                                                                    cur_temp_index] * 0.03)) / random.randint(
            1, 10)
    elif 23 < cur_temp <= 26:
        larvae -= ((temperature_change * temperature_larvae[cur_temp_index]) + (precipitation_change *
                                                                                temperature_larvae[
                                                                                    cur_temp_index] * 0.03)) / \
                  random.randint(1, 10)
        if larvae < 0:
            larvae = 0
    elif cur_temp <= 33:
        larvae -= (temperature_change * temperature_larvae[cur_temp_index]) + (precipitation_change *
                                                                               temperature_larvae[
                                                                                   cur_temp_index] * 0.03)
        if larvae < 0:
            larvae = 0
    else:
        larvae = 0
    return larvae


def calculate_mutated_caseload(cur_caseload: float, bites: float) -> int:
    """
    Calculate the number of cases in the system, given the current caseload.
    """
    return int(cur_caseload + infection_rate(bites))


def calculate_mutated_caseload_float(cur_caseload: float, bites: float) -> float:
    """
    Calculate the exact decimal representation of the caseload.
    Note: This function is provided for a more helpful
    visualization than what the last function is capable of.
    """
    return cur_caseload + infection_rate(bites)


def run_simulation() -> tuple:
    # baseline_temperatures is the montly average in Sylhet, Bangladesh.
    # baseline_precipitations is the monthly average in Sylhet, Bangladesh.
    # temperature_larvae is the larval population seen for temperatures in the range
    # 17 - 33 inclusive. Taken from
    # https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0079276, Results
    baseline_temperatures = [18, 20, 24, 26, 26, 27, 27, 28, 27, 26, 23, 19]
    baseline_precipitations = [11, 26, 105, 348, 557, 812, 800, 621, 513, 242, 25, 8]
    temperature_larvae = [650, 1100, 1500, 1750, 1850, 2000, 2100, 2250, 2250, 2150, 2050, 1950, 1750, 1500, 1250, 875,
                          250]
    baseline_caseload = 0

    cases_dict = {1: baseline_caseload}
    cases_dict_float = {1: baseline_caseload}
    day = 2
    while baseline_temperatures[0] <= 33:
        month = (day // 30) % 12
        baseline_temperature = baseline_temperatures[month]
        baseline_precipitation = baseline_precipitations[month]
        baseline_temperatures[month] = mutate_temperature(baseline_temperature, month)
        baseline_precipitations[month] = mutate_precipitation_level(baseline_precipitation, month)
        temperature_change = abs(baseline_temperatures[month] - baseline_temperature)
        precipitation_change = abs(baseline_precipitations[month] - baseline_precipitation)
        index_temperature_list = round(baseline_temperature) - 17
        if index_temperature_list >= 17:
            index_temperature_list = 0
        larva = mosquito_larvae_abundance(larvae=temperature_larvae[index_temperature_list],
                                          temperature=baseline_temperature,
                                          temperature_change=temperature_change,
                                          precipitation_change=precipitation_change)
        adult_mosquitoes = adult_mosquito_abundance(larva)
        bites = biting_rate(adult_mosquitoes)
        cases_dict[day] = calculate_mutated_caseload(cases_dict[day - 1], bites)
        cases_dict_float[day] = calculate_mutated_caseload_float(cases_dict_float[day - 1], bites)
        day += 1
    return (cases_dict, cases_dict_float)


def visualize_simulation() -> None:
    """
    Visualize the simulation in two different case scenarios that we explain in the project report.
    """
    import pandas
    import plotly.express as px

    main_dict = run_simulation()[0]
    main_dict_float = run_simulation()[1]
    days_list = [x for x in main_dict]
    cases_list = [main_dict[x] for x in main_dict]
    columns_data = {'days': days_list, 'cases': cases_list}
    df = pandas.DataFrame(columns_data, columns=['days', 'cases'])
    fig = px.scatter(df, x='days', y='cases')
    fig.show()

    case_change = {}
    for x in main_dict_float:
        if (x + 1) in main_dict_float:
            case_change[x + 1] = main_dict_float[x + 1] - main_dict_float[x]
    sec_days_list = [x for x in case_change]
    sec_cases_list = [case_change[x] for x in case_change]
    columns_data_2 = {'days': sec_days_list, 'case_change': sec_cases_list}
    df = pandas.DataFrame(columns_data_2, columns=['days', 'case_change'])
    fig = px.scatter(df, x='days', y='case_change')
    fig.show()
