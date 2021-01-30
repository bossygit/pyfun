import os
filename = input("Please enter the file name : ")
if not os.path.isfile(filename):
    file = open(filename,"w")
    notes = input("Enter your text : ")
    lines = []
    lines.append(notes)
    file.write(notes)
    file.write("\n")
    file.close()
else:
    choice = int(input("Type 1 to Read, 2 to Delete, 3 to Append or 4 to modify a line: "))
    if choice == 1:
        reader = open(filename,"r")
        lines = reader.readlines()
        for line in lines:
            print(line.strip("\n"))
        reader.close()
    if choice == 2:
        eraser = open(filename,"r+")
        notes = input("Enter your text : ")
        eraser.write(notes)
        eraser.write("\n")
        eraser.close()
    if choice == 3:
        updater = open(filename,"a")
        notes = input("Enter your text : ")
        updater.write(notes)
        updater.write("\n")
        updater.close()

    if choice == 4:
        liner = open(filename, "r+")
        lines = liner.readlines()
        print(lines)
        count = len(lines)
        num = int(input("There is {} lines choose the line to modify : ".format(count)))
        notes = input("Enter your text : ")
        lines[num-1] = notes + "\n"
        for line in lines:
            liner.write(line)
        print(lines)
        liner.close()




