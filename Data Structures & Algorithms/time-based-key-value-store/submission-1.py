class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map : return ""
        left, right = 0, len(self.map.get(key))-1
        res =""
        while left<=right:
            m = (left+right)//2
            if self.map[key][m][0] == timestamp: return self.map[key][m][1]
            if self.map[key][m][0] > timestamp:
                right = m-1
            else : 
                res = self.map[key][m][1]
                left = m+1
        return res

