class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:    
        min_speed = 1
        max_speed = max(piles)

        best_speed = max_speed
        while min_speed <= max_speed:
            mid = (min_speed + max_speed) // 2
            hours = 0
            for pile in piles:
                hours += pile // mid
                if pile % mid != 0:
                    hours += 1
            if hours <= h:
                best_speed = mid
                max_speed = mid - 1
            else:
                min_speed = mid + 1
        
        return best_speed