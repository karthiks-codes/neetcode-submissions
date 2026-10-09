class Solution:
    def numDecodings(self, s: str) -> int:
        dmap = {}
        dmap[len(s)] = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dmap[i] = 0
            else:
                dmap[i] = dmap[i + 1]

            if (i + 1) < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                dmap[i] += dmap[i + 2]

        return dmap[0]
        