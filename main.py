from itertools import chain
t1 = open('1.txt', 'r+', encoding='utf-8')
t2 = open('2.txt', 'r+', encoding='utf-8')
t3 = open('3.txt', 'r+', encoding='utf-8')

lst = []
for s in t1:
    s = s.rstrip()
    lst = lst + [s]

lst1 = []
for s in t2:
    s = s.rstrip()
    lst1 = lst1 + [s]

lst2 = []
for s in t3:
    s = s.rstrip()
    lst2 = lst2 + [s]


list_all = [lst, lst1, lst2]
all = sorted(list_all, key=len)

list1 = []
for x in all:
    list1.append(x)

items = list(chain(*list1))

items.insert(0, str(len(lst1)))
items.insert(0, t2.name)
items.insert(3, str(len(lst)))
items.insert(3, t1.name)
items.insert(13, str(len(lst2)))
items.insert(13, t3.name)


with open('finaltetxt.txt', 'w', encoding='utf-8' ) as fileall:
    fileall.writelines("%s\n" % line for line in items)

t1.close()
t2.close()
t3.close()



