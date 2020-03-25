"""
On a N * N grid, we place some 1 * 1 * 1 cubes.
Each value v = grid[i][j] represents a tower of v cubes placed on top of
grid cell (i, j)

Return the total surface area of the resulting shapes.


Example 1:

Input: [[2]]
Output: 10

Example 2:

Input: [[1, 2], [3, 4]]
Output: 34

Example 3:

Input: [[1, 0], [0, 2]]
Output: 16

Example 4:

Input: [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
Output: 46

Example 5:

Input: [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
Output: 32
"""
test_list = [
             [[2]],
             [[1, 2], [3, 4]],
             [[1, 0], [0, 2]],
             [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
             [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
             ]
ans = [10, 34, 16, 32, 46]


class Solution:
    def surface_area(self, grid) -> int:
        """

        :param grid:
        :return:
        """
        # areas = 0  # 最终形体的表面积
        # # 1. 顶部与底部的面积相同，只要单元格内有方格，就 + 1
        # for i in grid:
        #     for j in i:
        #         if j > 0:
        #             areas += 1

        N = len(grid)  # 网格的边长
        areas = 0  # 表面积
        for i in range(N):  # 遍历行，i为行标
            for j in range(N):  # 遍历列，j为列标
                # 1.顶部、底部的处理
                if grid[i][j] > 0:
                    areas += 2
                else:
                    continue
                # 2. 四周及内部的处理
                # 1> 首先判断该位置四周是否有其他方块
                for row, col in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                    if row in range(N) and col in range(N):  # 判断下标是否有效
                        areas += max(0, grid[i][j] - grid[row][col])
                    else:
                        areas += grid[i][j]

        return areas


if __name__ == "__main__":

    for i in range(5):
        grid = test_list[i]
        answer = ans[i]

        if Solution().surface_area(grid) != answer:
            print("程序有错误")
        else:
            print(f"Question{i + 1}: {test_list[i]}")
            print(f"answer: {answer}")

