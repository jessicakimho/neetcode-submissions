class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # cannot modify original array -> cannot sort
        # must use constant extra space -> no hashset
        # linkedlist cycle, floyds algo?

        # phase 1: where does fast and slow catch each other in the cycle?
        fast = slow = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # phase 2: where does the cycle begin? -> duplicate
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
