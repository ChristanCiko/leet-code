from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        vals = [0] * length
        stack = []  # 单调栈：先进后出

        # 从左至右算
        for i in range(length):
            tem = temperatures[i]
            while stack and tem > temperatures[stack[-1]]:  # 如果栈不为空，并且当前元素大于栈顶
                j = stack.pop()  # 那么栈顶出栈并记录
                vals[j] = i - j  # 那么对应的栈顶元素的结果计算就是i - j
            stack.append(i)  # 当前元素入栈
        return vals

if __name__ == '__main__':
    result = Solution().dailyTemperatures([73,74,75,71,69,72,76,73])
    print(result)
