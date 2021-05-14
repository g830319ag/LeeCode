class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        k=1
        output = 0
        while (N-(k+1)*k/2) >= 0:
            if (N-(k+1)*k/2) % k==0:
                output += 1
            k += 1
        return output
