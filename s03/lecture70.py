tempertures = [10, -20, -289, 100]

def c_to_f(c):
    if c < -273.15:
        return "That temperature is out of range (input is less than -273.15)"
    else:
        f = c * 9/5 + 32
        return f

with open("conversions.txt", "w") as output_file:
    for temperture in tempertures:
        converted = c_to_f(temperture)

        if type(converted) is str:
            print(converted)
        else:
            output_file.write(str(converted) + '\n')