class Solution:

    def twoSum(self,nums: List[int],target: int) -> List[int]:
        num_map = {} #空の辞書を作成
        for i, num in enumerate(nums): #インデックスと値を同時に取り出す
            complement = target - num
            if complement in num_map:
                return [num_map[complement],i]
            num_map[num] = i


