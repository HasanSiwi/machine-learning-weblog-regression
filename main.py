#Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# read the dataset, from a csv file
dataFile = pd.read_csv('weblog.csv', sep=',')

# this function will count how many rows contains the given month
def count_usage_per_month(data, month):

    timeArray = []

    for row in data['Time']:
        timeArray.append(row.split('/'))

    count = 0
    month_index = 1
    for elemnt in timeArray:
        if elemnt[month_index] == month:
            count+=1

    return count

# this will calculate the average usage of each month
def average_usage_per_month(col, condition):
    urlElements = (dataFile.loc[dataFile[col] == condition])

    janCount = count_usage_per_month(urlElements, 'Jan')
    febCount = count_usage_per_month(urlElements, 'Feb')
    marCount = count_usage_per_month(urlElements, 'Mar')
    aprCount = count_usage_per_month(urlElements, 'Apr')
    mayCount = count_usage_per_month(urlElements, 'May')
    junCount = count_usage_per_month(urlElements, 'Jun')
    julCount = count_usage_per_month(urlElements, 'Jul')
    augCount = count_usage_per_month(urlElements, 'Aug')
    sepCount = count_usage_per_month(urlElements, 'Sep')
    octCount = count_usage_per_month(urlElements, 'Oct')
    novCount = count_usage_per_month(urlElements, 'Nov')
    decCount = count_usage_per_month(urlElements, 'Dec')

    totalCount = janCount + febCount + marCount + aprCount + mayCount + julCount + julCount + augCount + sepCount + octCount + novCount + decCount

    janCountAvg = "{0:.2f}".format((janCount / totalCount)*100)
    febCountAvg = "{0:.2f}".format((febCount / totalCount)*100)
    marCountAvg = "{0:.2f}".format((marCount / totalCount)*100)
    aprCountAvg = "{0:.2f}".format((aprCount / totalCount)*100)
    mayCountAvg = "{0:.2f}".format((mayCount / totalCount)*100)
    junCountAvg = "{0:.2f}".format((junCount / totalCount)*100)
    julCountAvg = "{0:.2f}".format((julCount / totalCount)*100)
    augCountAvg = "{0:.2f}".format((augCount / totalCount)*100)
    sepCountAvg = "{0:.2f}".format((sepCount / totalCount)*100)
    octCountAvg = "{0:.2f}".format((octCount / totalCount)*100)
    novCountAvg = "{0:.2f}".format((novCount / totalCount)*100)
    decCountAvg = "{0:.2f}".format((decCount / totalCount)*100)

    averagePerMonth = [
        float(janCountAvg),
        float(febCountAvg),
        float(marCountAvg),
        float(aprCountAvg),
        float(mayCountAvg),
        float(junCountAvg),
        float(julCountAvg),
        float(augCountAvg),
        float(sepCountAvg),
        float(octCountAvg),
        float(novCountAvg),
        float(decCountAvg)
    ]

    return averagePerMonth

# will return the index of maximum element of the given array
def max_in_array(array):
    count = 0
    rush_month_index = 0

    for singleMonthAverage in avgPerMonth:
        if singleMonthAverage > array[rush_month_index]:
            rush_month_index = count
        count += 1

    return rush_month_index

def get_month_name(index):
    switcher = {
        0:  "January",
        1:  "February",
        2:  "March",
        3:  "April",
        4:  "May",
        5:  "June",
        6:  "July",
        7:  "August",
        8:  "September",
        9:  "October",
        10: "November",
        11: "December"
    }
    return switcher[index]

# this function will estimate coefficients of the given
# x = months and y = average per each month
def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)

    # mean of x and y vector
    m_x, m_y = np.mean(x), np.mean(y)

    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y * x) - n * m_y * m_x
    SS_xx = np.sum(x * x) - n * m_x * m_x

    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x

    return (b_0, b_1)


def plot_regression_line(x, y, b):
    # Scatter Plot
    plt.scatter(x, y, color="m", marker="o", s=30)

    # predicted response vector (Law)
    y_predicted = b[0] + b[1] * x

    # plotting the regression line
    plt.plot(x, y_predicted, color="r")

    # putting labels
    plt.xlabel('Month')
    plt.ylabel('Average')

    # function to show plot
    plt.show()


# Draw Plot of Time Series
def plot_time_series(x, y, title="", xlabel='Date', ylabel='Value', dpi=100):
    plt.figure(figsize=(16,5), dpi=dpi)
    plt.plot(x, y, color='tab:red')
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()



print('first of all, we can see some statistics about our data')
print(dataFile.describe())

print('\nYou can see that the most used URL is:')
print(dataFile.URL.mode())

print('--------------------')

avgPerMonth = average_usage_per_month("URL", dataFile.URL.mode()[0])

print('The average of all months is: ')
print(avgPerMonth)

print('--------------------')

print(get_month_name(max_in_array(avgPerMonth)), 'is the Rush Month.')
print('--------------------')

urlElements = (dataFile.loc[dataFile.URL == dataFile.URL.mode()[0]])

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

janCount = count_usage_per_month(urlElements, 'Jan')
febCount = count_usage_per_month(urlElements, 'Feb')
marCount = count_usage_per_month(urlElements, 'Mar')
aprCount = count_usage_per_month(urlElements, 'Apr')
mayCount = count_usage_per_month(urlElements, 'May')
junCount = count_usage_per_month(urlElements, 'Jun')
julCount = count_usage_per_month(urlElements, 'Jul')
augCount = count_usage_per_month(urlElements, 'Aug')
sepCount = count_usage_per_month(urlElements, 'Sep')
octCount = count_usage_per_month(urlElements, 'Oct')
novCount = count_usage_per_month(urlElements, 'Nov')
decCount = count_usage_per_month(urlElements, 'Dec')

months_count = [
    janCount,
    febCount,
    marCount,
    aprCount,
    mayCount,
    junCount,
    julCount,
    augCount,
    sepCount,
    octCount,
    novCount,
    decCount
]

averagePerMonths = avgPerMonth

# Normal Scatter Plot for the data
plt.scatter(months, averagePerMonths)
plt.xlabel("months")
plt.ylabel("average %")
plt.show()


# Our variables: (x = month , y = average per month)
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y = np.array(averagePerMonths)

# estimating
estimated_coefficient = estimate_coef(x, y)

print(
    "Estimated coefficients:\nb_0 = {}  \
    \nb_1 = {}".format(
        estimated_coefficient[0],
        estimated_coefficient[1]
    )
)

# plotting regression line
plot_regression_line(x, y, estimated_coefficient)

# plotting Time Series Algorithm
plot_time_series(x=x, y=y, title='Monthly Average visits for most frequent page (Login Page).')

