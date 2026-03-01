from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 获取矩阵的行数（高度）和列数（宽度）
        width = len(matrix)
        length = len(matrix[0])

        # 边界情况处理：如果矩阵为空（无行或无列），则无法构成正方形，返回面积 0
        if width == 0 or length == 0:
            return 0

        # 记录最大正方形的边长，初始为 0
        max_side = 0

        # 创建动态规划（DP）表，dp[i][j] 表示以 (i, j) 为右下角的最大全 1 正方形的边长
        # 初始化为与原矩阵相同大小的二维数组，所有值为 0
        dp = [[0] * length for _ in range(width)]

        # 遍历矩阵中的每一个元素
        for i in range(width):
            for j in range(length):
                # 只有当当前元素为 '1' 时，才可能扩展成正方形
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        # 如果在第一行或第一列，最大正方形只能是自身（边长为 1）
                        dp[i][j] = 1
                    else:
                        # 否则，状态转移方程：
                        # 当前位置的最大边长 = 上、左、左上三个方向的最小值 + 1
                        # 这保证了当前正方形是“全 1”的
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

                    # 更新全局最大边长
                    max_side = max(max_side, dp[i][j])

        # 返回最大正方形的面积（边长的平方）
        return max_side * max_side


# 主程序入口：用于测试函数
if __name__ == '__main__':
    s = Solution()
    # 测试用例：输入一个 2x2 的字符矩阵，输出最大全 1 正方形的面积
    print(s.maximalSquare([["0","1"],["1","0"]]))  # 输出: 1
