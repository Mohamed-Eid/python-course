#tuples: are immutable sequences
t = (1,"hi",True)
print(t[0])

# t[0]="test" tuples && strings is a immutable
print(t)

#===================================
#sets:are unordered collections of uniqe elements
x = set()
x.add(1)
x.add(2)
x.add(1)
x.add(0.1)
print(x)

list_set = set([1,1,1,1,1,2,2,2,2,2,3,3,3,4,4])
print(list_set)
