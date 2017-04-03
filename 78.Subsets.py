class Solution(object):
    """
    Medium
    """
    def subsets0(self, nums):
        """
        My solution
        AC
        好像做过这道题，思想是一个队列的形式（也不完全是队列，就算是一个列表吧），
        从前向后遍历，不断向队列增加元素。
        [[]]
        对于[]:插入[1],[2],[3]，此时队列为[[],[1],[2],[3]]
        对于[1]:插入[1,2],[1,3]，此时队列为[[],[1],[2],[3],[1,2],[1,3]]
        对于[2]:插入[2,3]，此时队列为[[],[1],[2],[3],[1,2],[1,3],[2,3]]
        对于[3]:不插入
        对于[1,2]：插入[1,2,3]，此时队列为[[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
        后面几个元素都跳过
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        stack = [[]]
        if not nums:
            return stack
        n = len(nums)
        for e in stack:
            for x in nums:
                if not e or x > e[-1]:
                    stack.append(e+[x])
        return stack

        # DFS recursively
    def subsets1(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in xrange(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)

    # Bit Manipulation
    def subsets2(self, nums):
        """
        还没有仔细理解哦
        :param nums:
        :return:
        """
        res = []
        nums.sort()
        for i in xrange(1<<len(nums)):
            tmp = []
            for j in xrange(len(nums)):
                if i & 1 << j:  # if i >> j & 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res

    # Iteratively
    def subsets(self, nums):
        res = [[]]
        for num in sorted(nums):
            res += [item+[num] for item in res]
        return res



s = Solution()
print(s.subsets1([1,2,3]))