class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        if len(strs) == 0 : return res
        for s in strs:
            res+= str(len(s))+'@#'+s
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        if s=="" : return res
        i = 0
        while i < len(s):
            j = i
            while s[j]!='@' or s[j+1]!='#':
                j+=1
            l = int(s[i:j])
            res.append(s[j+2: j+2+l])
            i = j+2+l
        return res
            
