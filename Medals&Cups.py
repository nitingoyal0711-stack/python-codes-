a1,a2,a3 = map(int,input().split())
b1,b2,b3 = map(int,input().split())
n =int(input())
 
total_cup = a1+a2+a3
total_medal =b1+b2+b3
 
shel_for_cups = (total_cup + 4)//5
shel_for_medals =(total_medals + 9)//10
 
if shel_for_medals +shel_for_cups <= n:
 print("YES")
else:
 print("NO")