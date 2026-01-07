class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        max_flip = 0
        
        for i, flip in enumerate(flips):
            max_flip = max(max_flip, flip)
            # After i+1 flips, if max_flip equals i+1, string is prefix-aligned
            if max_flip == i + 1:
                count += 1
        
        return count