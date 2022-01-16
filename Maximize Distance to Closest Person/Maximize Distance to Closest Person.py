class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        seats_adjusted= [1]
        seats_adjusted.extend(seats)
        seats_adjusted.extend([1])
        maxdistance = 0
        templeft = 0
        tempright = 0
        
        for i in range(len(seats_adjusted)):
            if seats_adjusted[i] == 1:
                #Handling ends
                if templeft == 0 or i == len(seats_adjusted)-1:
                    if  i - templeft-1 > maxdistance:
                        maxdistance = i - templeft-1
                else:
                    if (i - templeft) // 2 > maxdistance:
                        maxdistance = (i - templeft) // 2
                templeft = i
        return maxdistance