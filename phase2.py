import csv
import operator
from datetime import date
import matplotlib.pyplot as plt
import numpy as np
from collections import OrderedDict

def readDataFile():
    '''
    >>> a = readDataFile()
    >>> a[0:4]
    [['1869-01-01', '9.0'], ['1869-01-02', '0.0'], ['1869-01-03', '0.0'], ['1869-01-04', '0.0']]
    '''
    '''
    Function to read a csv file and store the data in a list
    Returns dataList, a list with values from the
    columns with index 2 and 4 from the file
    '''
    dataList= [] # initialize list for storing values
    with open("central_park.csv", newline='') as csvfile: # creates a file object
        csvreader = csv.reader(csvfile, delimiter=',')# set for reading csv file
        next(csvreader)
        for row in csvreader:
            s = row[2]
            if '-' in s:
                yr, mon, day = s.split('-')
                d = date(int(yr), int(mon), int(day))
            elif '/' in s:
                mon, day, yr = s.split('/')
            dataList += [[row[2], row[4]]] # saving columns with index of 2, 3, and 4
    return dataList # return a 2-D array with 3 columns

def days_of_snow(year):
    '''
    >>> days_of_snow('1869')
    10
    '''
    '''
    days_of_snow(year) intakes a string, year, and finds the number of days in said year that it snowed.
    '''
    dataList = readDataFile()
    snowDays = 0 
    for row in dataList:
        if year in row[0]:
            if row[1] != '0.0':
                snowDays = snowDays + 1
    return snowDays

def snow_dictionary():
    '''
    >>> a = snow_dictionary()
    >>> print(a)
    {'1869': [10], '1870': [9], '1871': [15],
    '1872': [17], '1873': [19], '1874': [9], '1875': [18],
    '1876': [16], '1877': [11], '1878': [8], '1879': [20],
    '1880': [14], '1881': [15], '1882': [17], '1883': [22], '1884': [19],
    '1885': [13], '1886': [14], '1887': [20], '1888': [14], '1889': [12],
    '1890': [13], '1891': [9], '1892': [20], '1893': [28], '1894': [18],
    '1895': [16], '1896': [26], '1897': [15], '1898': [20], '1899': [17],
    '1900': [10], '1901': [12], '1902': [17], '1903': [10], '1904': [28], '1905': [13],
    '1906': [8], '1907': [22], '1908': [17], '1909': [15], '1910': [12], '1911': [18],
    '1912': [70], '1913': [8], '1914': [26], '1915': [19], '1916': [30], '1917': [27],
    '1918': [17], '1919': [12], '1920': [25], '1921': [11], '1922': [16], '1923': [24],
    '1924': [18], '1925': [13], '1926': [26], '1927': [12], '1928': [8], '1929': [15],
    '1930': [12], '1931': [13], '1932': [11], '1933': [17], '1934': [12], '1935': [26],
    '1936': [18], '1937': [17], '1938': [19], '1939': [16], '1940': [17], '1941': [14],
    '1942': [21], '1943': [13], '1944': [13], '1945': [22], '1946': [9], '1947': [18],
    '1948': [26], '1949': [9], '1950': [13], '1951': [9], '1952': [17], '1953': [9], '1954': [12],
    '1955': [17], '1956': [17], '1957': [19], '1958': [17], '1959': [17], '1960': [22], '1961': [19],
    '1962': [19], '1963': [15], '1964': [21], '1965': [13], '1966': [16], '1967': [21], '1968': [11],
    '1969': [11], '1970': [15], '1971': [6], '1972': [11], '1973': [5], '1974': [14], '1975': [8],
    '1976': [13], '1977': [17], '1978': [16], '1979': [10], '1980': [9], '1981': [11], '1982': [10],
    '1983': [10], '1984': [19], '1985': [15], '1986': [11], '1987': [12], '1988': [9], '1989': [8],
    '1990': [7], '1991': [9], '1992': [6], '1993': [17], '1994': [20], '1995': [11], '1996': [20],
    '1997': [7], '1998': [3], '1999': [6], '2000': [11], '2001': [10], '2002': [4], '2003': [17],
    '2004': [15], '2005': [19], '2006': [5], '2007': [16], '2008': [8], '2009': [11], '2010': [12],
    '2011': [13], '2012': [5], '2013': [13], '2014': [17], '2015': [17], '2016': [10], '2017': [11], '2018': [10]}
    '''
    '''
    snow_dictionary() creates a dictionary with the year as the key and the number of days of snowfall.
    in said year as the value.
    '''
    snow_dict = {}
    dataList = readDataFile()
    for row in dataList:
        year = row[0].split('-')[0]
        if year not in snow_dict:
            snow_dict[year] = [days_of_snow(year)]
    return snow_dict

def sorted_snow():
    '''
    >>> a = sorted_snow()
    >>> print(a)
    ([1869, 1870, 1871, 1872, 1873, 1874,
    1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882, 1883,
    1884, 1885, 1886, 1887, 1888, 1889, 1890, 1891, 1892,
    1893, 1894, 1895, 1896, 1897, 1898, 1899, 1900, 1901,
    1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910,
    1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919,
    1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928,
    1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937,
    1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946,
    1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955,
    1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964,
    1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973,
    1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982,
    1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991,
    1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000,
    2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
    2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018],
    [10, 9, 15, 17, 19, 9, 18, 16, 11, 8, 20, 14, 15, 17,
    22, 19, 13, 14, 20, 14, 12, 13, 9, 20, 28, 18, 16, 26,
    15, 20, 17, 10, 12, 17, 10, 28, 13, 8, 22, 17, 15, 12,
    18, 70, 8, 26, 19, 30, 27, 17, 12, 25, 11, 16, 24, 18,
    13, 26, 12, 8, 15, 12, 13, 11, 17, 12, 26, 18, 17, 19,
    16, 17, 14, 21, 13, 13, 22, 9, 18, 26, 9, 13, 9, 17, 9,
    12, 17, 17, 19, 17, 17, 22, 19, 19, 15, 21, 13, 16, 21,
    11, 11, 15, 6, 11, 5, 14, 8, 13, 17, 16, 10, 9,
    11, 10, 10, 19, 15, 11, 12, 9, 8, 7, 9, 6, 17, 20, 11,
    20, 7, 3, 6, 11, 10, 4, 17, 15, 19, 5, 16, 8, 11, 12,
    13, 5, 13, 17, 17, 10, 11, 10])
    '''
    '''
    sorted_snow() returns a list of the integer keys and a list of the integer values in snow_dict.
    '''
    snow_dict = snow_dictionary()
    keys = []
    values = []
    for key, value in snow_dict.items():
        keys += [int(key)]
        values += [int(value[0])]
    return keys, values

def plot_yearly_snow():
    '''
    plot_yearly_snow() creates a bargraph of the yearly snowfall in New York from 1869-2018.
    '''
    keys, values = sorted_snow()
    x = list(keys)
    y = list(values)

    plt.bar(x,y)
    plt.subplots_adjust(bottom = 0.15)
    plt.xlabel('Year')
    plt.ylabel('Number of Days That it Snowed')
    plt.title('Number Days of Snow Fall per Year in New York 1869-2018')
    plt.show()
                



