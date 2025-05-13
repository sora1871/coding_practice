class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = {}
        count2 = {}

        for i in nums1:
            count1[i] = count1.get(i, 0) + 1

        for i in nums2:
            count2[i] = count2.get(i, 0) + 1    

        # キーの重複がないようにセットで比較
        keys1 = set(count1.keys())
        keys2 = set(count2.keys())

        return list(keys1 & keys2)
