class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0: return "EMPTY_LIST"
        coded = "/!*".join(list(strs))
        return coded

    def decode(self, s: str) -> List[str]:
        if s == "EMPTY_LIST":
            return []
        decoded = s.split("/!*")
        return decoded
