"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
"""
class Solution(object):
    # def partition(self, s):
    #     """
    #     my solution:
    #       想法和top solution一致，DFS，但是结果有错误。
    #     :type s: str
    #     :rtype: List[List[str]]
    #     """
    #     res = []
    #     new_res = []
    #     return self.DFS(s, res, new_res)
    #
    # def DFS(self, s, res, new_res):
    #     for i in range(len(s)):
    #         if self.isPalindrome(s[:i+1]):
    #             new_res.append(s[:i+1])
    #             self.DFS(s[i+1:], res, new_res)
    #             if i == len(s) - 1:
    #                 res.append(new_res)
    #                 new_res = []
    #     return res
    #
    # def isPalindrome(self, s):
    #     if not s:
    #         return True
    #     return s == s[::-1]

    def partition(self, s):
        """
        DFS
        :param s:
        :return:
        """
        ret = []
        for i in range(1, len(s)+1):
            if s[:i] == s[i-1::-1]:
                for rest in self.partition(s[i:]):
                    ret.append([s[:i]]+rest)
        if not ret:
            return [[]]
        return ret

s = Solution()
print(s.partition("aab"))