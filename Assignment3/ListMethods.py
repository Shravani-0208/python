l = ['Shravani','Shreya','Trupti']
print(l)
print("append() : \n", l.append('Srujana'))
print(l)

print("copy() : \n", l.copy())

l2 = [1,2,3,4,5,3,3,2,2,5,6,7]
print(l2)
print("count() : \n", l2.count(7))

print(l)
print(l2)
l.extend(l2)
print("Extend() : \n", l)

print(l)
print("index() : \n", l.index("Shreya"))

l3 = ["Sakshi","Radha","Priya","Vedu"]
print(l3)
l3.insert(3,"Riya")
print("index() : \n",l3)

print(l3)
l3.pop(3)
print("pop() : \n",l3)

print(l3)
l3.remove("Vedu")
print("remove() : \n",l3)

print(l)
l.reverse()
print("reverse() : \n",l)

print(l3)
l3.sort()
print("sort() : \n",l3) 
# NOT SUPPORT THE LIST CONTAINS INT  AND STRINGS