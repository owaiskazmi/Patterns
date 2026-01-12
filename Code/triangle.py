rows = int (input ("Enter number of rows: "))

print ()
for i in range (1, rows + 1):
    for j in range (0, i):
        print ("*", end = " ")
    print ()
print ()
