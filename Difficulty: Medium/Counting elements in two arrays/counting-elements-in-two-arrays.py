import bisect
class Solution:
    def countLessEq(self, l1, l2):
        # code here
        k = []
        l2.sort()
        for i in l1:
            index = bisect.bisect_right(l2,i)
            k.append(index)
        return k
        