class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
            
        nums = set(nums)

        startseq = defaultdict(list)
        seqcount = defaultdict(int)
        for i in nums:
            if (i - 1) not in nums:
                startseq[i].append(i)
                print(i)
                j = i
                while j in nums:
                    startseq[i].append(j)
                    seqcount[i] += 1
                    print(j)
                    j += 1

        return max(seqcount.values())
        

                
        

                    





        