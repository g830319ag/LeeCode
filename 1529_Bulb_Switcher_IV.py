class Solution:
    def minFlips(self, target: str) -> int:
        count = 0
        temp = 0
        for i in target:
            if int(i) != temp:
                temp = 1 - temp 
                count += 1
        return count
            
