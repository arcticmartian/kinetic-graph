import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as tck
# Installing python libraries:
# pip install matplotlib pandas
# python -m pip <library> linux
# py -m pip <library> Windows


# Open file, must be located in the same directory as the .py file
file_name = 'kinetics.csv' # The file in this directory

# Reads the file as a pandas data file
data = pd.read_csv(file_name, delimiter=';')


# Set the collors in hexadecimal or in english in case of basic colors  
axis_color = 'black'
data_color = '#1f77b4' # Blue
data_color2 = 'red'

# Create a figure and a set of subplots
fig, ax = plt.subplots()
# minor stiks 
ax.yaxis.set_minor_locator(tck.AutoMinorLocator())
ax.xaxis.set_minor_locator(tck.AutoMinorLocator())

# Set the columns in pandas. data.iloc[:,0] = columna 0
#x = data.iloc[:,0]
#y1 = data.iloc[:,1]
#y2 = data.iloc[:,2]

# Represents the graphs
# ax.plot(x, y, linestyle='', marker='', markevery='', markersize='', color='', label='')
ax.plot(data.iloc[:,0], data.iloc[:,1], linestyle='-', marker='D', markevery=9, markersize=4, color='#80ACA3', label='4 ºC [Asp-dNHS]')
ax.plot(data.iloc[:,0], data.iloc[:,2], linestyle='-', marker='s', markevery=9, markersize=4, color='#80ACA3', label='4 ºC [Asp-OSi]')

ax.plot(data.iloc[:,0], data.iloc[:,3], linestyle='-', marker='v', markevery=9, markersize=5, color='#88b984', label='21 ºC [Asp-dNHS]')
ax.plot(data.iloc[:,0], data.iloc[:,4], linestyle='-', marker='^', markevery=9, markersize=5, color='#88b984', label='21 ºC [Asp-OSi]')

ax.plot(data.iloc[:,0], data.iloc[:,5], linestyle='-', marker='*', markevery=9, markersize=7, color='#008080', label='30 ºC [Asp-dNHS]')
ax.plot(data.iloc[:,0], data.iloc[:,6], linestyle='-', marker='.', markevery=9, markersize=7, color='#008080', label='30 ºC [Asp-OSi]')
 

# First and last value of the first column.
#x1 = (data.iloc[:,1][0])
#x2 = (data.iloc[:,1][len(data.iloc[:,0]) - 1])

#y1 = (data.iloc[:,2][0])
#y2 = (data.iloc[:,2][len(data.iloc[:,2]) - 1])

# Also first and last value of the first column
columna = data.iloc[:,1]
x1 = (columna[1])
x2 = (columna[len(columna) - 1])

columna = data.iloc[:,2]
y1 = (columna[2])
y2 = (columna[len(columna) - 1])


# Graph limits
ax.set_xlim(0, 7170)
ax.set_ylim(0, 10)

# Aspect ratio, (x/y)/(aspect/ratio), if we want an aspect ratio of 16:9,
# 1) We calculate the difference between the limits in x (671 - 1) and multiply it by 9
# 2) We calculate the difference between the limits in y (67 - -40) and multiply it by 16
# (670/107)/(16/9).
ax.set_aspect((7171/10)/(16/9))

# For labels 
ax.set_xlabel('t (fs)', color=axis_color)
#ax.set_xlabel(data.columns[0], color=axis_color)
ax.set_ylabel('[Concentration]', color=axis_color)
ax.legend(frameon=False)

# Saves the generated graph in the same directory as the .py file
fig.savefig("kinetics.svg")
# Shows the graph in the .py file
plt.show()