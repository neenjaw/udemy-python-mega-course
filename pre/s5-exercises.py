def celsius_to_fahrenheit(c):
    if c < -273.15:
        return "Cannot be less than -273.15"
    else:
        f = (c * (9/5)) + 32
        return f

temperatures = [10,-20,-289,100]

for temperature in temperatures:
    print(celsius_to_fahrenheit(temperature))
