###Sukhdeep Kaur, HW#5, March 12th, 2025
import numpy as np
filename="vgsales-2.csv"
dtype=[('Name', object),('Year', int), ('NA_Sales', float)]
data = []
with open(filename, 'r') as file:
    next(file)
    for line in file:
        try:
            columns= line.strip().split(",") ###Learned to use both strip and split for proper splitting from the web.
            name= columns[1]
            year= int(float(columns[2]))
            NA_Sales= float(columns[6])
            data.append((name, year, NA_Sales))
        except ValueError:
            pass
data_array= np.array(data, dtype=dtype)  
sorted_data= np.sort(data_array, order=['Name', 'Year', 'NA_Sales'])

count = 0
for entry in sorted_data:
    print(entry)
    count+=1
    if count == 10:
        break
