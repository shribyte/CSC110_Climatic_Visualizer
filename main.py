from climatic_visualizer import *
from young_data_visualizer import *
from youth_data_visualizer import *
from middle_age_data_visualizer import *
from elder_data_visualizer import *
from simulation_cases import *


def run_project() -> None:
    data_list = read_csvfile('ClimateandinfectiousdiseaseCSV3.csv')
    new_list = list_helper(data_list)
    visualize()
    # visualize_young()
    # visualize_youth()
    # visualize_middle()
    # visualize_elder()
    visualize_temperature(new_list)
    visualize_humidity(new_list)
    visualize_precipitation(new_list)

    # this call runs the simulation, and visualizes it.
    visualize_simulation()


if __name__ == '__main__':
    run_project()
    # python_ta.check_all(config={
    #  'extra-imports': ['total_data_visualizer', 'youth_data_visualizer',
    #  'young_data_visualizer', 'elder_data_visualizer', 'simulation_cases', 'climatic_visualizer'],
    # the names (strs) of imported modules
    #    'allowed-io': [],  # the names (strs) of functions that call print/open/input
    #   'max-line-length': 100,
    #    'disable': ['R1705', 'C0200']
    # })
