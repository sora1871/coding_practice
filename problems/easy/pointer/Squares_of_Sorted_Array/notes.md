# Squares of a Sorted Array

## 問題リンク
[LeetCode #977 – Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)

---

## 問題概要

与えられた **昇順の整数配列 `nums`** に対し、  
**各要素の平方を計算し、それを昇順に並べた新しい配列を返す**。  
**in-place である必要はなく、新しいリストの返却でOK**。

---

## ✅ 解法バリエーション

### ✅ 解法1: `v1_sort_by_abs.py`（絶対値でソート → 2乗）

- `sorted(nums, key=abs)` で絶対値順にソートし、全要素を2乗
- シンプル・Pythonicで読みやすい
- 時間計算量：O(n log n)、空間計算量：O(n)

---

### ✅ 解法2: `optimal.py`（Two Pointers 最適解）

- `nums` は昇順 → 絶対値が大きいのは両端にある
- `left` / `right` ポインタで中央に向かい、`res[pos]` に大きい方を後ろから埋める
- 最適な時間計算量で動作
- 時間計算量：O(n)、空間計算量：O(n)

---

## ✅ 学び・気づき

- ソート済み配列 + 絶対値の処理は「2ポインタ戦略」の典型例
- `sorted()` による O(n log n) 解も悪くないが、**時間制約のある面接では最適解推奨**
- LeetCode で「in-place 操作」が指定されていない場合、新しい配列を返すのはOK
- Pythonでの平方は `x**2` もしくは `x * x` で計算可能（`math.pow` はfloatになるので注意）
