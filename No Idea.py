# Enter your code here. Read input from STDIN. Print output to STDOUT

l = list(map(int,input().split()))
n = l[0]
m = l[1]

array_input = list(map(int,input().split()))

a = list(map(int,input().split()))
b = list(map(int,input().split()))

aset = set()
bset = set()

for i in a:
    aset.add(i)
for j in b:
    bset.add(j)

happiness = 0
for k in array_input:
    if k in aset:
        happiness += 1
    if k in bset:
        happiness -= 1


print(happiness)