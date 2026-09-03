class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s.strip())
        n = len(chars)
        self.reverse(chars, 0, n - 1)
        self.reverse_each_word(chars)
        return self.clean_spaces(chars)
    def reverse(self, chars, left, right):
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
    def reverse_each_word(self, chars):
        n = len(chars)
        start = 0
        for end in range(n + 1):
            if end == n or chars[end] == ' ':
                self.reverse(chars, start, end - 1)
                start = end + 1
    def clean_spaces(self, chars):
        result = []
        i = 0
        n = len(chars)
        while i < n:
            if chars[i] != ' ':
                if result:
                    result.append(' ')
                while i < n and chars[i] != ' ':
                    result.append(chars[i])
                    i += 1
            else:
                i += 1
        return ''.join(result)