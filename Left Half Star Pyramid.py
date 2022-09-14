
Rows = int(input("Input Rows.."))

for x in range(Rows):
    for y in range(Rows-x-1):
        print(" ",end=" ")
    for z in range(x+1):
        print("*",end=" ")
    print()


