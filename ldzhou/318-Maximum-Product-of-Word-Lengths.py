# 这道题的思路比较常规, 唯一比较trick的地方就是, 将两个单词进行比较, 是否share字符的方法是, 将单词转成一个int表示, 这样就可以通过int的与操作, 快速判断
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ans = 0
        mask = [0] * len(words)
        words.sort(key=lambda k: len(k), reverse=True)
        for i in range(len(words)):
            word = words[i]
            for char in word:
                mask[i] |= 1 << (ord(char) - ord('a'))
        for i in range(len(words)):
            if len(words[i]) ** 2 <= ans:
                break
            for j in range(i + 1, len(words)):
                if (mask[i] & mask[j]) == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans
