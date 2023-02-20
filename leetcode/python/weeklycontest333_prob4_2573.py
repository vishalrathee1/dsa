class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        s = [0]*len(lcp)
        c = 1
        for i in range(len(lcp)):
            #checks if ith char in string is already constructed or not
            if s[i] : continue
            #if c exceeds 'z' return ""
            if c>26: return ""
            #constructs the jth char of string based on ith row traversal
            for j in range(i, len(lcp)):
                if lcp[i][j]!=0:
                    s[j]=c
            c+=1

        #checking if the string constructed has the same value as given lcp
        for i in range(len(lcp)):
            for j in range(len(lcp)):
                val = lcp[i+1][j+1] if i+1<len(lcp) and j+1<len(lcp) else 0
                val = val+1 if s[i]==s[j] else 0
                if val!=lcp[i][j]:
                    return ""
        return "".join(chr(ord('a')+i-1) for i in s)