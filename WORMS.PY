N= map(int,input().split())
a = list(map(int,input().split()))

prefix = []
total = 0
for x in a :
    total += x
    prefix.append(total)   

m = int(input())
queries = list (map(int,input().split()))
for q in queries :
    left = 0 
    right = N- 1
    
    while left <= right:
        mid = (left + right)

        if prefix[mid] >= q:
            right = mid - 1

        else:
            left = mid +1

    print(left +1)         