from collections import Counter
a = int(input())
b = list(map(int,input().split()))
d = Counter(b)

ss = set(b)
for i in ss:
    if(d[i] == 1):
        print(i)
        break;
