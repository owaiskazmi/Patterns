# 🎨 Patterns Repo

This repository contains simple **Python programs** to generate different patterns, and number sequences. Perfect for beginners learning **loops** and **basic Python programming**. 🐍✨

---

## 📂 Programs Included
 
1. [Triangle](#triangle) 🔺  
2. [Numbers in Descending Order](#numbers-in-descending-order) 🔢  
3. [Inverted Triangle](#inverted-triangle) 🔻
---

## Patterns Included

### 🔺 Triangle
Prints a right-angled triangle of stars based on the number of rows.

### Code Overview
```bash
rows = int (input ("Enter number of rows: "))
print ()
for i in range (1, rows + 1):
    for j in range (0, i):
        print ("*", end = " ")
    print ()
print ()
```

### Example Output
[![Triangle](https://github.com/owaiskazmi/Patterns/blob/main/Screenshots/triangle.png)](https://github.com/owaiskazmi/Patterns/blob/main/Screenshots/triangle.png)

### 🔢 Numbers in Descending Order
Prints numbers in a descending order pattern.

### Code Overview
```bash
print ("Numbers in Descending Order")
print ()
num = int (input ("Enter a number: "))
print ()
for i in range (num, 0, -1):
    for j in range (i, 0, -1):
        print (j, end = " ")
    print ()
print ()
```

### Example Output
[![Numbers](https://github.com/owaiskazmi/Patterns/blob/main/Screenshots/numbers.png)](https://github.com/owaiskazmi/Patterns/blob/main/Screenshots/numbers.png)

### 🔻 Inverted Triangle
Prints an inverted triangle of stars based on the number of rows.

### Code Overview
```bash
print ("Inverted Triangle")
print ()
rows = int (input ("Enter number of rows: "))
print ()
for i in range (rows, 0, -1):
    print ("* " * i)
print ()
```

### Example Output
[![Inverted Triangle](https://github.com/owaiskazmi/Patterns/blob/main/Screenshots/inverted_triangle.png)](https://github.com/owaiskazmi/Patterns/blob/main/Screenshots/inverted_triangle.png)

## Purpose
These programs help practice:
- Loops and nested loops
- Printing and formatting output
- Logic building
- Problem-solving skills

This repo is part of my learning journey as a high school ICS student exploring programming concepts.
