import array
# mengoncersi string ke array.array
B = array.array('b')
B.fromstring('Python')

for karakter in B:
    print('%c' % karakter, end=' ')