import array
# mengonversi list ke array.array
li = [10,20,30,40,50]

C = array.array('i')
C.fromlist(li)
print(type(C))

for nilai in C:
    print('%d' % nilai, end= ' ')