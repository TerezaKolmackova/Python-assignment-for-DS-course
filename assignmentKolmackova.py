#Python assignment for the course Data Steward, Module 2
#Tereza Kolmačková
#Date: 2025-01-07

import numpy
import matplotlib.pyplot as plt

#Reading data from a file
data = numpy.loadtxt(fname='WeatherData.txt', delimiter=',', skiprows=1)

#Diagram for humidity
time = data[0:,0]
humidity = data[0:,4]
plt.plot(time, humidity)
plt.xlabel("Time [h]")
plt.ylabel("Humidity [%]")
plt.grid()
plt.show()

#Calculating the mean temperature
def calculate_mean_temperature(filename):
    temperatures = []

    with open(filename, 'r') as file:
        header = file.readline()  # skip header line

        for line in file:
            columns = line.strip().split(',')
            temperature = float(columns[3]) 
            temperatures.append(temperature)

    mean_temperature = sum(temperatures) / len(temperatures)
    return mean_temperature

if __name__ == "__main__":
    filename = "WeatherData.txt"
    mean_temp = calculate_mean_temperature(filename)
    print(f"Mean ambient air temperature is {mean_temp:.2f} °C.")
    
#Calculating hours with temperature below 0
def count_hours_below_zero(filename):
    count = 0

    with open(filename, 'r') as file:
        header = file.readline()  # skip header line

        for line in file:
            columns = line.strip().split(',')
            temperature = float(columns[3])
            if temperature < 0:
                count += 1

    return count

hours_below_zero = count_hours_below_zero(filename)
print(f"Number of hours with temperature below 0°C is {hours_below_zero}.")