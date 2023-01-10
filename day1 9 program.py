time=int(input())
entry=list(map(int, input().split()))
exit=list(map(int, input().split()))
present=0
total_guests=0
for i in range(time):
    present += entry[i]-exit[i]
    if Total_guests < Present:
        Total_guests = Present
print(Total_guests, end = " ")
