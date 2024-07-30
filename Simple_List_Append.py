
# Using a for loop, write a program that:
# -	Reads a first list of values from the user using the input().split() function. The list will contain positive and negative values.
# -	Creates a second list with the list() function and populates with the positive values of the first list. Use the .append() function. 
# -	Print the first and second list.

first=input("Enter a value: ").split()
n=len(first)
for i in range (n):
    first[i]=int (first [i])

second=list()
for i in range(n):
    if first[i]>0:
       second.append(first[i])
print (first,second)
