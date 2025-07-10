class Solution():
    def longestString(self, arr):
        # code here
        arr.sort()
        # print(arr)
        prev = arr[0]
        m = ""
        for word in arr[1:]:
            if word[:-1] == prev:
                if len(m) < len(word):
                    m = word 
            prev = word
      
        return m