#1)Take input of two integer lists and Concatenate two lists index-wise:

# suppose the user gives inputs such as a = [4, 3, 6] and b = [7. 2, 11]
# the output should be = [11, 5, 17]. Make sure you consider the corner cases

a = [4, 3, 6] 
b = [7, 2, 11]
c = []
for i in range (len(a)):
    d = a[i]+b[i]
    c.append(d)
print(c)    






