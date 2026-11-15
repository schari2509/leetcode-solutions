from collections import Counter, defaultdict
from typing import List


class Solution:

    # Time Complexity: O(wordLen * (N / wordLen) * wordLen) = O(N * wordLen) where N = len(s).
    # Slicing words of length wordLen takes O(wordLen), and each word is visited at most twice.
    # Space Complexity: O(M * wordLen) where M = len(words), for storing word counts in hash maps.
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        numWords = len(words)
        wordLen = len(words[0])
        totalLen = numWords * wordLen
        indices = []

        if len(s) < totalLen:
            return indices

        wordsCount = Counter(words)

        for offset in range(wordLen):
            left, right = offset, offset
            windowCount = defaultdict(int)
            count = 0

            while right + wordLen <= len(s):
                sub = s[right : right + wordLen]
                right += wordLen

                if sub in wordsCount:
                    windowCount[sub] += 1
                    count += 1

                    # If there are more occurrences than required, shrink from left
                    while windowCount[sub] > wordsCount[sub]:
                        leftWord = s[left : left + wordLen]
                        windowCount[leftWord] -= 1
                        left += wordLen
                        count -= 1

                    # If all words matched, record the starting index
                    if count == numWords:
                        indices.append(left)
                        firstWord = s[left : left + wordLen]
                        windowCount[firstWord] -= 1
                        left += wordLen
                        count -= 1
                else:
                    # Invalid word encountered: reset window
                    count = 0
                    left = right
                    windowCount.clear()

        return indices
