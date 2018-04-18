# myfile = open("example.txt", "w")
# myfile.write("something")
# myfile.close()

with open("example.txt", "w") as myfile:
    myfile.write("something else")