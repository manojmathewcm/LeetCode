class Solution:
    def minDays(self, n: int) -> int:
        q = [[n]]
        days = 0
        fl = False

        while q:
            stepList = q[0]
            newStep = set()
            for num in stepList:
                if not num % 2:
                    newStep.add(num/2)
                if not num % 3:
                    newStep.add(num/3)
                if num == 1:
                    fl = True
                    break
                newStep.add(num - 1)
            days += 1
            if fl:
                break
            q.append(list(newStep))
            del(q[0])
        
        return days

#Breadth first search starting from n with 3 options (1 per day, 1/2 per day, 2/3 per day).
