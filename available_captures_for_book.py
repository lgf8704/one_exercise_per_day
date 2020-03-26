"""
On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns. 
These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces,
and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south),
then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored
pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/available-captures-for-rook
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Example 1:

Input: [
[".",".",".",".",".",".",".","."],
[".",".",".","p",".",".",".","."],
[".",".",".","R",".",".",".","p"],
[".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".","."],
[".",".",".","p",".",".",".","."],
[".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".","."]
]

Output: 3
Explanation:
In this example the rook is able to capture all the pawns.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/available-captures-for-rook
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def num_rook_captures(board) -> int:

        # 定义能捕获的卒子数量
        res = 0

        # 找到'R'的位置
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    row, col = i, j

        # 沿着四个方向寻找
        for x, y in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # x, y 分别对应行标、列表变化的方向，0不变，1变大， -1变小
            r = row + x
            c = col + y

            while r in range(8) and c in range(8):
                cell = board[r][c]
                if cell == 'B':
                    break
                elif cell == '.':
                    r += x
                    c += y
                elif cell == 'p':
                    res += 1
                    break

        print(res)


if __name__ == "__main__":

    board = [
[".",".",".",".",".",".",".","."],
[".",".",".","p",".",".",".","."],
[".",".",".","R",".",".",".","p"],
[".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".","."],
[".",".",".","p",".",".",".","."],
[".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".","."]
]
    Solution.num_rook_captures(board)
