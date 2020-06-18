class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not haystack:
            return -1
        if not needle:
            return 0

        return haystack.find(needle)
