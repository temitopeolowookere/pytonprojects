import random

lst = list(range(1,11))
print(lst)

random.shuffle(lst)

print(lst)

#lst.append(20)
#print(lst)
#lst.append(40)

#print(lst)

#lst.extend([30,50,60])

#print(lst)

#lst.append([80])
#print(lst)

lst +=[20,30,40]
print(lst)

lst.insert(-1,56)
print(lst)

lst.append(15)
print(lst)

last_item = lst.pop()
print(last_item)

print(lst)

item_at_index_5 = lst.pop(5)
print(lst)

print("count",lst.count(8))

lst.remove(8)
print(lst)

# lst.clear()
# print(lst)

lst.reverse()
print(lst)




