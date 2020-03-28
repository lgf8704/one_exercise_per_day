"""
Given a list of words, we may encode it by writing a reference string S and a list of indexes A.

For example, if the list of words is ["time", "me", "bell"], we can write it as S = "time#bell#"
and indexes = [0, 2, 5].

Then for each index, we will recover the word by reading from the reference string from that index until
we reach a "#" character.

What is the length of the shortest reference string S possible that encodes the given words?

Example:

Input: words = ["time", "me", "bell"]
Output: 10
Explanation: S = "time#bell#" and indexes = [0, 2, 5].



Note:

    1 <= words.length <= 2000.
    1 <= words[i].length <= 7.
    Each word has only lowercase letters.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/short-encoding-of-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:

        words_set = set(words)
        # 遍历单词列表
        for word in list(words_set):
        # 1. 删除单词的后缀单词（从下标1开始）
            for k in range(1, len(word)):
                words_set.discard(word[k:])
        # 2. 生成res
        res = sum([len(word) + 1 for word in words_set])
        # 3. 返回res
        return res