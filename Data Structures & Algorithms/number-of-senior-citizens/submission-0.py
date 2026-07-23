class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for i in details:
            j = int(i[11:13])
            if j > 60:
                ans +=1

        return ans


        