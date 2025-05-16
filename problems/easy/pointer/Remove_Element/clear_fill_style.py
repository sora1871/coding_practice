class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        insert_pos = 0
        for num in nums:
            if num != val:
                nums[insert_pos] = num
                insert_pos += 1

        for i in range(insert_pos, len(nums)):
            nums[i] = val

        return insert_pos
