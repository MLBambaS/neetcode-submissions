class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res+=str(len(s))+'@#'+s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        if s=='': return res
        i=0
        while (i<len(s)):
            j=i
            while s[j:j+2] !='@#':
                j+=1
            n=int(s[i:j])
            res.append(s[j+2:j+2+n])
            i=j+2+n
        return res