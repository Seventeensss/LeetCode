class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        My solution
        AC
        《剑指offer上的题》，记得大概解题思路，but...应该只对比右上角就够了，还是做麻烦了
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix) - 1
        if n < 0:
            return False
        m = len(matrix[0]) - 1
        if m < 0:
            return False
        i, j = 0, 0
        while i < n or j < m:
            while matrix[i][m] > target and m > 0:
                m -= 1
            while matrix[n][j] > target and n > 0:
                n -= 1
            while matrix[i][m] < target and i < n:
                i += 1
            while matrix[n][j] < target and j < m:
                j += 1
            if matrix[n][m] < target:
                return False
            if matrix[n][m] == target or matrix[n][j] == target or matrix[i][m] == target:
                return True
        return matrix[n][m] == target

    def searchMatrix1(self, matrix, target):
        """
        只对比右上角
        :param matrix:
        :param target:
        :return:
        """
        m = len(matrix)
        if m <= 0:
            return False
        n = len(matrix[0])
        if n <= 0:
            return False
        r, c = 0, n - 1
        while r < m and c >= 0:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target:
                c -= 1
            else:
                r += 1
        return False


s = Solution()
print(s.searchMatrix(
        [[5,6,9],[9,10,11],[11,14,18]],9))