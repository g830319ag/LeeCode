class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        step = 0
        for i, num in enumerate(nums):
            if step>i+num and num==0:
                continue
            step = max(step, i+num)
            if num==0 and step < len(nums)-1:
                return False
            elif step >= len(nums)-1:
                return True
