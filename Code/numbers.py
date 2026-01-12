print ("Numbers in Descending Order")
print ()
num = int (input ("Enter a number: "))
print ()
for i in range (num, 0, -1):
    for j in range (i, 0, -1):
        print (j, end = " ")
    print ()
print ()
