def find_in_file(f):
    myfile = open("sample.txt")
    fruits = myfile.read()
    fruits = fruits.splitlines()

    if f in fruits:
        return "Fruit found"
    else:
        return "No such fruit found!"

address = ["Flat Floor Street", "18", "New York"]
pins = {"Mike":1234, "Joe":1111, "Jacko":4444}

print(address[0], address[1])

pin = int(input("Enter your pin: "))

if pin in pins.values():
    fruit = input("Enter fruit: ")
    print(find_in_file(fruit))
else:
    print("Incorrect")
    print("This info can be accessed only by: ")
    for key in pins.keys():
        print(key)