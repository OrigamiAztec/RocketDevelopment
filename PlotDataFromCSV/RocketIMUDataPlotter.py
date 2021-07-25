# Input : csv file with time, altitude, temp, pressure, and acceleration.
# Output : HTML files with plots and hover tools to analyze data quickly.
# Author : Antonio Diaz, antonio.diaz.hsa@gmail.com, Instagram : @ChileanAstro
# Date Last Edited : July 25, 2021
 
# step 1: pip install bokeh
# step 2: pip install pandas
# step 3: paste all data from the excel sheet to a new notepad file and saved it as 'DATALOG.csv'
#   I'm also assuming the labels will always be 'Milliseconds', 'Altitude', 'Temperature', and so on exactly typed like that.
# step 4: put csv file in the same folder as this python file. Example: RocketIMUDataPlotter.py in download folder and DATALOG.csv in same folder.
# step 5: change line 17 to your data file name if different. Example: C:\Users\Username\Downloads\LOGGEDDATA.txt

import pandas as pd
from bokeh.models import HoverTool
from bokeh.plotting import figure, show
from bokeh.models.widgets import Panel, Tabs

dataFileFormatted = pd.read_csv('DATALOG.csv', dialect='excel-tab')
timeData = dataFileFormatted['Milliseconds']
altitudeData = dataFileFormatted['Altitude']
tempData = dataFileFormatted['Temperature']
pressureData = dataFileFormatted['Pressure']
accelXData = dataFileFormatted['AccelX']
accelYData = dataFileFormatted['AccelY']
accelZData = dataFileFormatted['AccelZ']
maxAccelZData = dataFileFormatted['MaxAccelZ']
altitudeStartData = dataFileFormatted['AltitudeStart']

data = dict(time=timeData, altitude=altitudeData, temperature = tempData, pressure = pressureData, accelX = accelXData, accelY = accelYData, accelZ = accelZData, maxAccelZ = maxAccelZData, altitudeStart = altitudeStartData)
hover_tool_1 = HoverTool(tooltips = [("time", "@time{0.}"),("altitude", "@altitude{0.00}")], names = ["line_section1"], mode = "vline")
fig1 = figure(title="Altitude vs Time", x_axis_label='time (ms)', y_axis_label='Altitude (Meters)')
fig1.add_tools(hover_tool_1)
fig1.line('time', 'altitude', source = data, name = "line_section1")
fig1.dot(timeData, altitudeData, size = 15)
tab1 = Panel(child=fig1, title = "Altitude")

fig2 = figure(title="Temp vs Time", x_axis_label='time (ms)', y_axis_label='Temperature (Celsius)')
hover_tool_2 = HoverTool(tooltips = [("time", "@time{0.}"),("Temperature", "@temperature{0.00}")], names = ["line_section2"], mode = "vline")
fig2.add_tools(hover_tool_2)
fig2.line('time', 'temperature', source = data, name = "line_section2")
fig2.dot(timeData, tempData, size = 15)
tab2 = Panel(child=fig2, title = "Temperature")

fig3 = figure(title="Pressure vs Time", x_axis_label='time (ms)', y_axis_label='Pressure (hPa)')
hover_tool_2 = HoverTool(tooltips = [("time", "@time{0.}"),("pressure", "@pressure{0.00}")], names = ["line_section3"], mode = "vline")
fig3.add_tools(hover_tool_2)
fig3.line('time', 'pressure', source = data, name = "line_section3")
fig3.dot(timeData, pressureData, size = 15)
tab3 = Panel(child=fig3, title = "Pressure")

fig4 = figure(title="Acceleration vs Time", x_axis_label='time (ms)', y_axis_label='Acceleration (g-force multiplier)')
hover_tool_3 = HoverTool(tooltips = [("time", "@time{0.}"),("accelX", "@accelX{0.00}"), ("accelY", "@accelY{0.00}"), ("accelZ", "@accelZ{0.00}")], names = ["line_section4"], mode = "vline")
fig4.add_tools(hover_tool_3)
fig4.line('time', 'accelX', source = data, color="red")
fig4.line('time', 'accelY', source = data, color="green")
fig4.line('time', 'accelZ', source = data, name = "line_section4", color="black")
fig4.dot(timeData, accelXData, color="red", size = 15)
fig4.dot(timeData, accelYData, color="green", size = 15)
fig4.dot(timeData, accelZData, color="black", size = 15)
tab4 = Panel(child=fig4, title = "Acceleration")

fig5 = figure(title="Max Z Acceleration vs Time", x_axis_label='time (ms)', y_axis_label='Acceleration (g-force multiplier)')
hover_tool_5 = HoverTool(tooltips = [("time", "@time{0.}"),("max Z Accel", "@maxAccelZ{0.00}")], names = ["line_section5"], mode = "vline")
fig5.add_tools(hover_tool_5)
fig5.line('time', 'maxAccelZ', source = data, name = "line_section5")
fig5.dot(timeData, maxAccelZData, size = 15)
tab5 = Panel(child=fig5, title = "Max Acceleration")

fig6 = figure(title="Altitude vs Time", x_axis_label='time (ms)', y_axis_label='Altitude Start (meters)')
hover_tool_6 = HoverTool(tooltips = [("time", "@time{0.}"),("pressure", "@altitudeStart{0.00}")], names = ["line_section6"], mode = "vline")
fig6.add_tools(hover_tool_6)
fig6.line('time', 'altitudeStart', source = data, name = "line_section6")
fig6.dot(timeData, altitudeStartData, size = 15)
tab6 = Panel(child=fig6, title = "Altitude Start")

tabs = Tabs(tabs=[tab1, tab2, tab3, tab4, tab5, tab6])
show(tabs)