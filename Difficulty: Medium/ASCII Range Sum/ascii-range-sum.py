class Solution:
    def asciirange(self, s):
        # code here
        prefix = []
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = [i]
            else:
                d[s[i]].append(i)
            if prefix == []:
                prefix.append(ord(s[i]))
            else:
                prefix.append(prefix[-1] + ord(s[i]))
        
        result = []

        for value in d.values():
            if len(value) >= 2:
                if value[-1] - 1 != value[0]:
                    result.append(prefix[value[-1]-1]-prefix[value[0]])

        return result