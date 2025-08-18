class Solution:
    def search(self, txt, pat):
        # code here
        indexes = []
        for i in range(len(txt)-len(pat)+1):
            if txt[i:i+len(pat)] == pat:
                indexes.append(i)
        return indexes
        