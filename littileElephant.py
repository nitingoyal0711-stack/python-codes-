n = int(input())
times = list(map(int,input().split()))

mn = min(times)

if times.count(mn) > 1:
    print("Still Rozdin")

else:
    print(times.index(mn)+1)