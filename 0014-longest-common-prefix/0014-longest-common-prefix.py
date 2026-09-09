class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1,len(strs)):
            current_word = strs[i]
            while not current_word.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix