class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)> len(s):
            return ""
        need = {}
        for ch in t:
            need[ch] = need.get(ch,0)+1
        window = {}
        have = 0
        required = len(need)
        l = 0
        res = ""
        res_len = float("inf")
        for r in range(len(s)):
            ch = s[r]
            window[ch] = window.get(ch,0)+1
            if ch in need and window[ch] == need[ch]:
                have+=1
            while have == required:
                if r-l+1 < res_len:
                    res_len = r-l+1
                    res = s[l:r+1]
                left_char = s[l]
                window[left_char]-=1
                if left_char in need and window[left_char]< need[left_char]:
                    have-=1
                l+=1
        return res