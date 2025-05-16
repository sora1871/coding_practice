# Contains Duplicate

##  問題リンク
[Contains Duplicate – LeetCode #217](https://leetcode.com/problems/contains-duplicate/)

---

##  問題概要

整数配列 `nums` が与えられる。  
同じ要素が2回以上含まれていれば `True` を返し、すべて異なれば `False` を返す。

---

## ✅ 解法バリエーション

### ❌ v1_bruteforce.py
- 全ての組み合わせ `(i, j)` を比較（`i != j`）
- 計算量：O(n²)
- 無駄な比較が多い（`(i, j)` と `(j, i)` の重複）

### ✅ v2_bruteforce_improved.py
- `(i < j)` に制限することで、比較回数を半分に減らした
- それでも O(n²)

### ✅ optimal.py
- `set` を使って、既に出現した要素を記録
- 各要素に対して `num in seen` で重複チェック（O(1))
- 計算量：O(n)、空間：O(n)
- **最適解であり、実務でもよく使われるパターン**

---

## ✅ 学び・気づき

- `set` は重複を許さない性質がある
- Python の `in` 演算子は `set` に対して O(1) で探索できる
- 二重ループはまず疑って、もっと効率的な手段がないか考えるべき

---

## ✅ テストケース例

```python
assert Solution().containsDuplicate([1, 2, 3, 1]) == True
assert Solution().containsDuplicate([1, 2, 3, 4]) == False
assert Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True
