# greeting = input("Write a greeting: ")

# print(greeting)

# a = 2
# b = 3
# print(a+b)

# if type(2) is int:
#     print("hi")

# age = int("28") + 50
# print(age)
# age = float(age)
# print(age)

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Zero division is meaningless."

print(divide(1,0))

