class TimeMap:
    # variant: finding the rightmost value satisfying a condition

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # create a list if this key doesnt exist yet
        if key not in self.timemap:
            self.timemap[key] = []
        # append the [value, timestamp]
        self.timemap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # retrieve history for the requested key
        values = self.timemap.get(key, []) # gets values for that key, or returns empty list
        # bin search the values
        left, right = 0, len(values) - 1
        res = ""

        while left <= right:
            mid = (left + right) // 2
            mid_timestamp = values[mid][1]
            if mid_timestamp <= timestamp: # found valid candidate, keep searching to the right
                res = values[mid][0]
                left = mid + 1

            else: # mid too large, search to the left
                right = mid - 1

        return res



        
