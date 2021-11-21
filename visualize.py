from climate_analysis import *
import numpy as np
import matplotlib.pyplot as plt


def sorted_yearly_temps():
    years = Yearly_av_temp_dictionary()
    keys = []
    values = []
    for key, value in years.items():
        keys += [int(key)]
        values += [int(value[0])]
    return keys, values

def sorted_DoN():
    over90 = daysOverNinety()
    keys = []
    values = []
    for key, value in over90.items():
        keys += [int(key)]
        values += [int(value[0])]
    return keys, values


def plot_average_yearly_temps():
    keys, values = sorted_yearly_temps()
    x = list(keys)
    y = list(values)
    plt.plot(x,y,'o')
    plt.subplots_adjust(bottom = 0.15)
    plt.xlabel('Year')
    plt.ylabel('Temperature')
    plt.title('Average Yearly Temperature in Central Park')
    plt.show()

def plot_num_DoN():
    keys, values = sorted_DoN()
    x = list(keys)
    y = list(values)
    plt.plot(x,y,'o')
    plt.subplots_adjust(bottom = 0.15)
    plt.xlabel('Year')
    plt.ylabel('Number of Days >= 90 Degrees F')
    plt.title('Average Number of Days >= 90 Degrees F')
    plt.show()
    
def plot_over90_yearly_temps():
    KEYS2, VALUES2 = mostOverNinety()
    x = list(KEYS2)
    y = list(VALUES2)
    plt.bar(x,y)
    plt.subplots_adjust(bottom = 0.15)
    plt.xlabel('Year')
    plt.ylabel('Number of Days >= 90 Degrees F')
    plt.title('20 Years with Top Number of Days >= 90 Degrees F')
    plt.show()
