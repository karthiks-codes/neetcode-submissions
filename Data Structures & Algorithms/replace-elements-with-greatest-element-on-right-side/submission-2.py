class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n
        maxi = -1
        for i in range(n - 1, -1, -1):
            ans[i] = maxi
            maxi = max(maxi, arr[i])

        return ans
            

        

        