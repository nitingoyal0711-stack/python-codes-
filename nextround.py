k,s= map(int,input().split())
a =list(map(int,input().split()))
count = 0
s_num = a[s-1]
for i in a:
    if i >= s_num and i > 0 :
        count += 1
        print(count)