#reads each line to an element in a list
file = open("fruit.txt", "r")

content = file.readlines()

file.close()

#strip the \n from the line in the list
content = [i.rstrip("\n") for i in content]

print(content)

######################################################################

# read the file as a whole to a string
file = open("fruit.txt", "r")

content = file.read()

file.close()

#will treat the string as an array of characters, run the rstrip, return a list of characters
content = [i.rstrip("\n") for i in content]

print(content)

######################################################################

#reads each line to an element in a list
file = open("fruit.txt", "r")

content = file.readlines()

file.close()

#strip the \n from the line in the list
content = [i.rstrip("\n") for i in content]

for item in content:
     print(len(item))

######################################################################

file = open("example.txt", "w") # open file to write (over)

file.write("Line 1")

file.close()

file = open("example.txt", "a") # open file to write (over)

file.write("Line 2")

file.close()

# r  - read         - pointer at beginning
# r+ - read/write   - pointer at beginning
# w  - write        - pointer at beginning, overwrites, creates new
# w+ - write/read   - pointer at beginning, overwrites, creates new
# a  - append       - pointer at end
# a+ - append/read  - pointer at end


######################################################################

with open("example.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    file.write("\nLine 6")
