import array

# 9.9
A = array.array('i', [100,200,300,400,500])
print(A)

A[1] = -700
A[4] = 800

print(A)

# 9.10
# print('Nilai awal')
# print(A)

# membalik urutan array
A.reverse()

# setelah dibalik
print('Setelah dibalik')
print(A)