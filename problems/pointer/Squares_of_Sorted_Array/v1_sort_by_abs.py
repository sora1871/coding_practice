# 解法1: 絶対値でソートして2乗
# - absで並び替えてから二乗する。
# - 時間計算量: O(n log n)、空間計算量: O(n)
def v1_sort_by_abs(nums):
    sorted_nums = sorted(nums, key=abs)  # 絶対値でソート
    for i in range(len(sorted_nums)):
        sorted_nums[i] = sorted_nums[i] ** 2  # 各要素を二乗
    return sorted_nums
