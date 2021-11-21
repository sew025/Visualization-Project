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
    [['1869-01-01', '29', '19'],
    ['1869-01-02', '27', '21'], ['1869-01-03', '35', '27'],
    ['1869-01-04', '37', '34']]
    '''
    '''
    Function to read a csv file and store the data in a list
    Returns dataList, a list with values from the
    columns with index 2, 6, and 7 from the file
    '''
    dataList= [] # initialize list for storing values
    with open("central_park.csv", newline='') as csvfile: # creates a file object
        csvreader = csv.reader(csvfile, delimiter=',')# set for reading csv file
        next(csvreader)
        max_temps = []
        min_temps = []
        for row in csvreader:
            s = row[2]
            max_temps += [row[6]]
            if '-' in s:
                yr, mon, day = s.split('-')
                d = date(int(yr), int(mon), int(day))
            elif '/' in s:
                mon, day, yr = s.split('/')
            dataList += [[row[2], row[6], row[7]]] # saving columns with index of 2, 3, and 4
    return dataList # return a 2-D array with 3 columns


def dailyAvgTemp(year):
    '''
    >>> dailyAvgTemp('1870')
                     
    [38.5, 46.0, 38.0, 32.0, 30.5, 37.5, 30.5, 26.0, 22.5, 31.5, 38.0, 46.0, 41.5,
     24.0, 39.5, 42.0, 46.5, 42.0, 36.0, 36.5, 38.0, 37.5, 51.0, 42.0, 42.0, 45.0, 43.5,
     36.5, 36.5, 39.0, 32.5, 29.0, 32.5, 30.5, 21.5, 26.0, 31.0, 33.5, 30.0, 30.5, 32.0,
     30.0, 38.0, 29.5, 35.5, 41.0, 37.5, 38.0, 42.0, 29.5, 31.0, 14.0, 16.0, 28.5, 24.5,
     22.0, 32.0, 30.5, 32.0, 34.0, 27.5, 27.5, 24.5, 26.5, 28.5, 30.5, 31.0, 30.0, 33.0,
     28.5, 28.0, 27.0, 32.5, 36.0, 33.0, 25.0, 34.0, 36.5, 41.0, 47.0, 44.0, 35.0, 35.5,
     35.5, 35.5, 41.5, 43.5, 44.0, 45.0, 46.5, 46.0, 41.5, 41.0, 34.0, 35.5, 40.5, 45.0,
     54.0, 55.0, 52.0, 46.0, 55.0, 56.5, 64.5, 62.0, 45.0, 44.5, 50.5, 45.5, 50.0, 50.5,
     52.0, 52.5, 55.0, 51.5, 56.5, 63.5, 66.0, 50.5, 55.5, 58.5, 62.5, 58.5, 67.0, 55.5,
     58.5, 56.0, 52.5, 53.5, 48.5, 48.0, 57.0, 61.0, 67.0, 73.5, 74.5, 58.0, 57.5, 65.0,
     70.0, 68.0, 61.5, 60.5, 68.0, 70.5, 63.5, 55.0, 55.0, 59.0, 60.5, 63.0, 65.5, 68.5,
     64.5, 70.0, 69.5, 73.0, 69.5, 75.5, 68.5, 66.0, 60.5, 67.0, 67.5, 73.5, 74.5, 75.5,
     72.5, 78.5, 79.5, 78.5, 66.5, 67.0, 77.0, 82.5, 84.5, 77.5, 76.5, 84.0, 83.5, 80.5,
     72.0, 67.5, 61.5, 67.5, 70.0, 75.0, 74.5, 70.0, 71.0, 74.0, 78.0, 79.5, 78.5, 80.5,
     77.5, 79.5, 87.5, 84.5, 83.5, 75.5, 81.0, 79.0, 83.0, 84.5, 85.5, 85.0, 75.5, 75.5,
     80.5, 73.0, 74.5, 76.0, 79.0, 79.0, 76.5, 76.0, 81.5, 82.0, 79.5, 80.5, 80.0, 78.5,
     80.5, 73.0, 65.5, 70.0, 72.5, 74.5, 76.5, 79.5, 78.0, 72.5, 70.0, 69.5, 71.5, 80.5,
     69.5, 66.0, 67.0, 77.0, 74.0, 71.0, 73.0, 74.0, 73.0, 72.0, 67.5, 66.5, 69.0, 65.5,
     63.5, 67.5, 61.0, 63.5, 65.5, 69.0, 68.0, 72.0, 66.0, 69.0, 64.0, 64.0, 65.5, 62.5,
     68.5, 74.5, 76.5, 69.0, 70.0, 69.5, 68.0, 66.5, 69.5, 62.5, 60.5, 65.5, 61.5, 55.5,
     52.0, 56.5, 59.5, 60.0, 60.5, 66.0, 58.0, 57.0, 59.0, 62.0, 61.0, 55.0, 48.0, 58.5,
     51.0, 54.0, 53.5, 56.5, 59.5, 49.5, 44.5, 53.5, 46.0, 43.0, 53.5, 50.0, 54.5, 53.5,
     50.5, 51.5, 43.5, 47.0, 48.0, 55.0, 41.0, 43.5, 49.5, 49.0, 46.5, 41.0, 38.5, 41.5,
     39.5, 31.0, 36.5, 44.5, 41.0, 45.0, 40.0, 42.0, 44.0, 51.0, 52.0, 54.0, 43.5, 42.0,
     46.5, 44.0, 48.5, 49.0, 45.0, 41.5, 41.5, 38.0, 36.5, 34.5, 46.5, 46.5, 41.0, 33.5,
     28.0, 29.0, 33.5, 34.5, 40.0, 28.5, 22.0, 20.5, 19.5, 20.0, 26.5, 24.5, 26.5, 17.5,
     20.0, 35.5]
    '''
    '''takes in a year and goes through the daily min and max
    temperatures for each day of the year. Then it returns an integer which
    would be the average temperature for each day of that year. '''
    avgDailyTemp = []
    with open("central_park.csv", newline='') as csvfile:
        csvreader=csv.reader(csvfile, delimiter=',')
        next(csvreader)
        for row in csvreader:
            
            if year in row[2]:
                if row[6] == '':
                    row[6] = 0
                if row[7] == '':
                    row[7] = 0
                else:
                    a = row[6]
                    b = row[7]
                    c = (int(a) + int(b)) / 2
                avgDailyTemp += [c]
    return avgDailyTemp

def yearlyAvgTemp(year):
    '''
    >>> yearlyAvgTemp('1869')
		 
    51.57397260273972
    '''
    '''calls dailyavgTemp and finds the average of the list that is produced.
    Produces an integer that finds the average of the year that is inputed.'''
    a = dailyAvgTemp(year)
    year_ave = sum(a)/len(a)
    return year_ave

def Yearly_av_temp_dictionary():
    '''
    Yearly_av_temp_dictionary() creates a dictionary with each year as the key and the average temperature
    for the given year as its value.
    '''
    years={}
    dataList = readDataFile()
    for row in dataList:
        year = row[0].split('-')[0]
        if year not in years:
            years[year] = [yearlyAvgTemp(year)]
    return years


def hottestOfTheYears():
    '''
    >>> a = hottestOfTheYears()
    >>> print(a)
    ([2018, 2012, 1991, 1990, 1998, 2016, 1953, 1949, 2006, 2015, 2010, 1999, 2011, 2002, 2017, 2001, 1973, 1983, 1931, 1979], [58.726072607260726, 57.36612021857923, 57.29178082191781, 57.28630136986301, 57.227397260273975, 57.21584699453552, 57.134246575342466, 56.98082191780822, 56.912328767123284, 56.83561643835616, 56.81095890410959, 56.54931506849315, 56.51917808219178, 56.48082191780822,
    56.40958904109589, 56.3, 56.175342465753424, 56.05205479452055, 55.87671232876713, 55.85616438356164])
    '''
    '''takes in a dictionary and orders it so that the values are from
    highest to lowest. Then returns lists of the 
    first twenty sorted keys and values in the new sorted dictionary'''
    years = Yearly_av_temp_dictionary()
    count = 0
    keys = []
    values = []
    sorted_years={}
    sorted_years = OrderedDict(sorted(years.items(), key = lambda kv: kv[1], reverse = True))
    for key, value in sorted_years.items():
        keys += [int(key)]
        values += [float(value[0])]
        count += 1
        if count == 20:
            break
    return keys, values

def print_hottest_years():
    '''
    >>> print_hottest_years()
       20 Hottest Years
    Year          Average Yearly Temperature F
    -----------------------------
     2018     58.726073   
     2012     57.366120   
     1991     57.291781   
     1990     57.286301   
     1998     57.227397   
     2016     57.215847   
     1953     57.134247   
     1949     56.980822   
     2006     56.912329   
     2015     56.835616   
     2010     56.810959   
     1999     56.549315   
     2011     56.519178   
     2002     56.480822   
     2017     56.409589   
     2001     56.300000   
     1973     56.175342   
     1983     56.052055   
     1931     55.876712   
     1979     55.856164  
    '''
    '''
    print_hottest_years() creates a table that represents the data of the 20 Hottest Years in our data set
    '''
    keys, values = hottestOfTheYears()
    print('   20 Hottest Years')
    print('Year          Average Yearly Temperature F')
    print('-----------------------------')
    for i in range(len(keys)):
        print('{0:5d}  {1:12f}   '.format(keys[i], values[i]))
        
def max_temp_dictionary():
    '''
    max_temp_dictionary() creates a dictionary with the keys as the years in the dataset and the values
    as the max temp on each day in that year.
    '''
    dataList = readDataFile()
    max_dict = dict()
    for row in dataList:
        year = row[0][0:4]
        if not year in max_dict:
            max_dict[year] = [int(row[1])]
        else:
            if row[1]:
                max_dict[year] += [int(row[1])]
    return max_dict

def daysOverNinety():
    '''
    daysOverNinety() creates a new dictionary with the keys as each year in the data set and the values
    as the number of days over 90 degrees in the given year.
    '''
    over90 = dict()
    max_dict = max_temp_dictionary()
    for i in max_dict:
        days = 0
        if not i in over90:
            for j in max_dict[i]:
                if j >= 90:
                    days = days + 1
                else:
                    days = days
            over90[i] = [days]
        else:
            over90[i] = []
    return over90


def mostOverNinety():
    '''
    >>> a = mostOverNinety()
    >>> print(a)
    ([1991, 1993, 1944, 2010, 1983, 1966, 1953, 1980, 1988, 2002, 1941, 1949, 1961, 1995, 1943, 1959, 1999, 1936, 1955, 1896],
    [39, 39, 37, 37, 36, 35, 32, 32, 32, 32, 29, 29, 29, 29, 28, 27, 27, 26, 25, 24])
    '''
    '''
    mostOverNinety() sorts the dictionary over90 from highest to lowest values and
    returns a list of the first 20 keys and values.
    '''
    over90 = daysOverNinety()
    sorted_DoN={}
    Keys = []
    Values = []
    count = 0
    sorted_DoN = OrderedDict(sorted(over90.items(), key = lambda kv: kv[1], reverse = True))
    for key, value in sorted_DoN.items():
        Keys += [int(key)]
        Values += [int(value[0])]
        count += 1
        if count == 20:
            break
    return Keys, Values

def print_DoN():
    '''
    >>> print_DoN()
       20 Years with Highest # of Days >= 90 Degrees
    Year          # of Days >= 90 degrees F
    -----------------------------
     1991            39   
     1993            39   
     1944            37   
     2010            37   
     1983            36   
     1966            35   
     1953            32   
     1980            32   
     1988            32   
     2002            32   
     1941            29   
     1949            29   
     1961            29   
     1995            29   
     1943            28   
     1959            27   
     1999            27   
     1936            26   
     1955            25   
     1896            24   
    '''
    '''
    print_DoN() creates a table that represents the data of the 20 years with the most days of 90
    degrees in our data set
    '''
    keys, values = mostOverNinety()
    print('   20 Years with Highest # of Days >= 90 Degrees')
    print('Year          # of Days >= 90 degrees F')
    print('-----------------------------')
    for i in range(len(keys)):
        print('{0:5d}  {1:12d}   '.format(keys[i], values[i]))
def main():
    '''
    main() calls the necessary functions to print the data tables that show the 20 Hottest Years in
    our data set and the 20 Years with Highest # of Days >= 90 Degrees in our data set.
    '''
    '''
       20 Hottest Years
    Year          Average Yearly Temperature F
    -----------------------------
     2018     58.726073   
     2012     57.366120   
     1991     57.291781   
     1990     57.286301   
     1998     57.227397   
     2016     57.215847   
     1953     57.134247   
     1949     56.980822   
     2006     56.912329   
     2015     56.835616   
     2010     56.810959   
     1999     56.549315   
     2011     56.519178   
     2002     56.480822   
     2017     56.409589   
     2001     56.300000   
     1973     56.175342   
     1983     56.052055   
     1931     55.876712   
     1979     55.856164   
       20 Years with Highest # of Days >= 90 Degrees
    Year          # of Days >= 90 degrees F
    -----------------------------
     1991            39   
     1993            39   
     1944            37   
     2010            37   
     1983            36   
     1966            35   
     1953            32   
     1980            32   
     1988            32   
     2002            32   
     1941            29   
     1949            29   
     1961            29   
     1995            29   
     1943            28   
     1959            27   
     1999            27   
     1936            26   
     1955            25   
     1896            24  
     '''
    dataList = readDataFile()
    print_hottest_years()
    print_DoN()

main()
    
