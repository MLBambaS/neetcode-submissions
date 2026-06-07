class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: return ''
        res = []
        for s in strs:
            code = str(len(s))+'!#'+s
            res.append(code)
        return ''.join(res)


    def decode(self, s: str) -> List[str]:
        if s=='': return []
        res = []
        i=0
        while i<len(s):
            j=i
            while s[j]!='!'and s[j+1]!='#':
                j+=1
            l = int(s[i:j])
            res.append(s[j+2: j+2+l])
            i = j+l+2
        return res


