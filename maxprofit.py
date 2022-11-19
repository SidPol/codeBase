n = int(input())
cost = input().split()
cost = [int(i) for i in cost]
result = [[-1]*(n+1)]*(n+1)
result[0] = [0]*(n+1)
for i in range(n+1):
    result[i][0] = 0
def findcost(inch,length):
    global result
    if result[inch][length] != -1:
        return result[inch][length]
    if length < inch:
        result[inch][length] = findcost(inch-1,length)
    result[inch][length] = max(findcost(inch-1,length),cost[inch-1]+findcost(inch,length-inch))
    return result[inch][length]
findcost(n,n)
print(result[n][n])