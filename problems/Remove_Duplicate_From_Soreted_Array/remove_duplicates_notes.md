# Remove Duplicates from Sorted Array

##  問題リンク
[LeetCode #26 - Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

---

##  問題概要

昇順にソートされた配列 `nums` から、**重複を in-place で削除**し、**重複なしの要素数 `k` を返す**。  
最初の `k` 要素にユニークな値を前方に詰め、残りの要素は無視される。

---

## ✅ 解法バリエーション

### ❌ v1_wrong_assignment.py.py
- `if i = j:` としてしまい、構文エラー
- `i` と `j` を「インデックス」として比較しているが、比較すべきは **値**（`nums[i] != nums[j]`）
- ロジックが未完成で先に進めない

---

### ✅ v2_optimal_two_pointers.py.py
- `j` を「次のユニーク要素の書き込み位置」として使う
- `i` で走査し、ユニークな要素があれば `j` を進めて書き込み
- 完全に in-place で処理（追加の配列を使わず O(1) 空間）
- 戻り値は `j + 1`（0ベースインデックスのため）

---

## 🧪 ステップ実行例

```python
nums = [0,0,1,1,2]
       ↑     ↑
       j     i
# nums[i] != nums[j] → jを1つ進め、nums[j] = nums[i]
# → 最終的に nums[:3] = [0, 1, 2]
```

---

## ✅ 学び

- `=` は代入、`==` は比較 → 基本の文法ミスに注意
- 2ポインタ法で in-place 更新することで O(n) 時間 + O(1) 空間で処理できる
- ソート済み配列だからこそ「重複が隣同士になる」特徴を活かせる

---
