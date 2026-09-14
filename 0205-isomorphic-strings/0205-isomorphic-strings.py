class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapS = {}
        mapT = {}
        for i in range(len(s)):
            charS = s[i]
            charT = t[i]
            if charS in mapS and mapS[charS]!= charT:
                return False
            if charT in mapT and mapT[charT]!=charS:
                return False
            mapS[charS] = charT
            mapT[charT] = charS
        return True