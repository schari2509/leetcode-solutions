from collections import Counter, defaultdict


class Solution:

    # Time Complexity: O(|S| + |T|) where |S| and |T| are the lengths of strings s and t respectively.
    # In the worst case, each character in s is visited at most twice (by left and right pointers).
    # Space Complexity: O(|Σ|) = O(1) auxiliary space, at most 52 unique English letters stored in maps.
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(t) > len(s):
            return ''

        tCounts = Counter(t)
        required = len(tCounts)

        left, right = 0, 0
        windowCounts = defaultdict(int)
        formed = 0
        minLen = float('inf')
        minLenIndices = None

        while right < len(s):
            char = s[right]
            windowCounts[char] += 1
            if char in tCounts and tCounts[char] == windowCounts[char]:
                formed += 1

            while formed == required:
                if (right - left + 1) < minLen:
                    minLen = right - left + 1
                    minLenIndices = (left, right)

                if s[left] in tCounts and windowCounts[s[left]] == tCounts[s[left]]:
                    formed -= 1

                windowCounts[s[left]] -= 1
                left += 1

            right += 1

        return '' if minLenIndices is None else s[minLenIndices[0]:minLenIndices[1] + 1]
