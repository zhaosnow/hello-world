class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int 
        """
        citations.sort()
        for i in range(len(citations)):
            citation = citations[i]
            num = len(citations) - i
            if num <= citation:
                return num
        return 0
