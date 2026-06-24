class TimeMap:

    def __init__(self):
        self.dic = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        
        self.dic[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        values = self.dic[key]
        lo, hi = 0, len(values) - 1
        res = ""
        while lo <= hi:
            mid = (hi + lo) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
            
                lo = mid + 1
            else:
                hi = mid - 1
        
        return res
        
