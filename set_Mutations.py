n_a_number = int(input())
a = set(list(map(int,input().split())))
n = int(input())
for i in range(n):
    k = list(input().split())
    operation = k[0]
    value = int(k[1])
    ss = set(list(map(int,input().split())))
    if(operation == 'intersection_update'):
        a.intersection_update(ss)
        continue
    if(operation == 'symmetric_difference_update'):
        a.symmetric_difference_update(ss)
        continue
    if(operation == 'difference_update'):
        a.difference_update(ss)
        continue
    if(operation == 'update'):
        a.update(ss)
        continue
kk = sum(a)
print(kk)