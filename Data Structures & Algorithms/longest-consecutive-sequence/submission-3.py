class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        nums = set(nums)

        seqcount = defaultdict(int)
        for i in nums:
            if (i - 1) not in nums:
                j = i
                while j in nums:
                    seqcount[i] += 1
                    j += 1
        return max(seqcount.values())
        

                
        

                    





        