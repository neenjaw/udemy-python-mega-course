def celsius_to_fahrenheit(c):
    if c < -273.15:
        return "Cannot be less than -273.15"
    else:
        f = (c * (9/5)) + 32
        return f

temperatures = [10,-20,-289,100]

file = open("example.txt", "w") # open file to write (over)


for temperature in temperatures:
    result = celsius_to_fahrenheit(temperature)
    if type(result) == float:
        file.write(str(result) + "\n")

file.close()
