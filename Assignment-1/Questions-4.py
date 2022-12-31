#4)Remove all occurrences of a specific item from a list:
list1 = [5, 20, 15, 20, 25, 50, 20]
list2=[]
for j in list1:
    if j ==20:
        continue
    list2.append(j)
print("New list after removing all Duplicate numbers: ", list2)