class Solution:
    def minWindow(self, s1, s2):
        # Code here
        n, m = len(s1), len(s2)
        min_len = float("inf")
        start = -1

        i = 0
        while i < n:
            j = 0
            # Step 1: forward match
            while i < n:
                if s1[i] == s2[j]:
                    j += 1
                    if j == m:
                        break
                i += 1

            if j < m:
                break  # no more subsequences possible

            # Step 2: backward shrink
            end = i
            j -= 1
            while j >= 0:
                if s1[i] == s2[j]:
                    j -= 1
                i -= 1
            i += 1  # correct overshoot

            # update answer
            if end - i + 1 < min_len:
                min_len = end - i + 1
                start = i

            i += 1  # move forward for next search

        return "" if start == -1 else s1[start:start + min_len]
