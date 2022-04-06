import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#utilize these libraries for later use
os.chdir("/Users/mac/documents/pycharm/practical7")
#import the table file in practical7 folder
covid_data = pd.read_csv("full_data.csv")
#use pandas library to read the table file "full_data.csv"
print(covid_data.iloc[10:21, [0, 2]])
#use pandas library to show the first and third columns from rows 10-20(inclusive)


n = 0
my_rows = []
#identify n as an integer
while n < 7996:
    if covid_data.loc[n, "location"] == "Afghanistan":
        covid_data.loc[n, "location"] = True
    else:
        covid_data.loc[n, "location"] = False
    my_rows = list(covid_data.loc[:, "location"])
    n = n+1
#complete a loop with n from 0 to 7995(all rows) using 'while'
#use if-else to judge whether the location of every row is Afghanistan
#if it is Afghanistan, mark it with True
#if not, mark it with False
#then put all Trues and Fasles into a new list called my_rows
print(covid_data.loc[my_rows, "total_cases"])
#use pandas to read every row, if 'my_rows' is True, then print its 'total_cases'
#if not, it is not necessary to print this row

covid_data = pd.read_csv("full_data.csv")
china_data = []
#make a list to store data of china
loca = list(covid_data.loc[:, "location"])
#put all locations into the list 'loca'
for i in range(0, len(loca)):
    china_data.append(loca[i] == "China")
#put all rows with location 'China' into the 'china_data' list
print(covid_data.loc[china_data, :])

mean = np.mean(covid_data.loc[china_data, ['new_cases', 'new_deaths']])
print(mean)
#use numpy library to measure the means of new cases and new deaths of china
#new_cases=893.923913 new_deaths=35.967391

x = covid_data.loc[china_data, ['new_cases', 'new_deaths']]
plt.boxplot(x, vert=True, whis=1.5, patch_artist=True, meanline=False, showbox=True, showcaps=True, showfliers=True, notch=False)
plt.title('new cases and deaths of China')
#label the boxplot with title 'new cases and deaths of China')
plt.show
#use matplotlib library to draw the boxplot of new cases and deaths in China

china_dates = covid_data.loc[china_data, "date"]
china_new_cases = covid_data.loc[china_data, "new_cases"]
china_new_deaths = covid_data.loc[china_data, "new_deaths"]
#make three lists to store dates, new cases and new deaths respectively to make plots
plt.plot(china_dates, china_new_cases, 'b+', label='new_cases')
#use blue '+' to show china new cases and label it
plt.plot(china_dates, china_new_deaths, 'r+', label='new_deaths')
#use red '+' to show china new deaths and label it
plt.title("new cases and deaths of China")
#name this plot
plt.xticks(china_dates.iloc[0:len(china_dates):4], rotation=-90)
#mark every 4 date at x-axis
#'rotation=-90' means turning the date marked on the x-axis 90 degrees clockwise
plt.legend
plt.show

plt.plot(china_dates, china_new_deaths/china_new_cases, 'bo', label="china_new_deaths/china_new_cases")
plt.ylabel("new_deaths/new_cases")
plt.xticks(china_dates.iloc[0:len(china_dates):4], rotation=-90)
plt.legend
plt.show
#make a plot with y-axis labeled 'new_deaths/new_cases' and x-axis labeled 'china_new_deaths/china_new_cases'

#Question 1 in the guidance: How have new cases and total cases developed over time in Spain?
spain_data = []
#make a list 'spain_data' to store the data of Spain
locat = list(covid_data.loc[:, "location"])
for i in range(0, len(locat)):
    spain_data.append(locat[i] == "Spain")
print(covid_data.loc[spain_data, ['new_cases', 'total_cases']])
#put all locations into the 'locat' list
#add rows about Spain into the 'spain_data' and print out 'new_cases' and 'total_cases'

spain_dates = covid_data.loc[spain_data, "date"]
spain_new_cases = covid_data.loc[spain_data, "new_cases"]
spain_total_cases = covid_data.loc[spain_data, "total_cases"]
#make three lists to store dates, new cases and new deaths respectively to make plots
plt.plot(spain_dates, spain_new_cases, 'b+', label="new_cases")
#use blue '+' to show Spain new cases and label it
plt.plot(spain_dates, spain_total_cases, 'r+', label="total_cases")
#use red '+' to show Spain total cases and label it
plt.title("new cases and total cases developed over time in Spain")
#name this plot
plt.xticks(spain_dates.iloc[0:len(spain_dates):4], rotation=-90)
#mark every 4 date at x-axis
#'rotation=-90' means turning the date marked on the x-axis 90 degrees clockwise
plt.legend
plt.show





