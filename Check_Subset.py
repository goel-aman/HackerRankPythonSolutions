t = int(input())
for w in range(t):
    no_of_element_a = int(input())
    a_set = set(list(map(int,input().split())))
    no_of_element_b = int(input())
    b_set = set(list(map(int,input().split())))
    c = 1
    for x in a_set:
        if(x in b_set):
            continue
        else:
            c = 0
            print("False")
            break
    if(c == 1):
        print("True")