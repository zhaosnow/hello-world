class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = dict()
        for str in strs:
            string = ''.join(sorted(str))
            if string in d:
                d[string].append(str)
            else:
                d[string] = [str]
        ans = list()
        for string in d:
            ans.append(d[string])
        return ans
