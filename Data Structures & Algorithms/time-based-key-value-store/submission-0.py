class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.store.get(key) is None:
            self.store[key] = []
        self.store.get(key).append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        output_lst = self.store.get(key, [])
        if output_lst == []:
            return res
        
        l = 0 
        r = len(output_lst) - 1
        while l <=r:
            m = (l + r) // 2
            if output_lst[m][1] <= timestamp:
                res = output_lst[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

        
