# Two Sum（ハッシュ探索の基本）

## 問題概要

整数の配列 `nums` と整数 `target` が与えられる。  
和が `target` になる 2つの要素のインデックスを返す。

---

## 解法①：2重ループ（Brute Force）

- **方法**：全てのペアを試す
- **計算量**：O(n²)
- **コード**：
  ```python
  for i in range(len(nums)):
      for j in range(i+1, len(nums)):
          if nums[i] + nums[j] == target:
              return [i, j]
学び：

シンプルだけど遅い

同じ要素を2回使わないよう j は i+1 から開始

解法②：辞書による補数探索（最適解）
方法：target - num の補数を辞書で探索

計算量：O(n)

コード：

```python
num_map = {}
for i, num in enumerate(nums):
    comp = target - num
    if comp in num_map:
        return [num_map[comp], i]
    num_map[num] = i
```
学び：

辞書（ハッシュ）を使えば検索は O(1)

辞書の中身は「数値 → インデックス」

辞書に追加するタイミングが重要（同じ要素を2回使わないよう注意）

振り返り・気づき
最初は値とインデックスを混同して nums[i] を誤って使っていた

for i in nums はインデックスじゃなく「値」を取ってる点に注意

dict に補数を保存 → 一瞬で探索できるという考え方は「型」として覚えておく
