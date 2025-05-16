# Remove Element

## 問題リンク
[LeetCode #27 – Remove Element](https://leetcode.com/problems/remove-element/)

---

## 問題概要

指定の値 `val` を配列 `nums` から in-place ですべて削除し、  
削除後の配列の長さを返す。戻り値以降の要素はどうでもよいが、`val` を含んではいけない。  
**追加メモリを使わずに操作することが要求される。**

---

## ✅ 解法バリエーション

### ✅ 解法1: two_pointers_forward.py（左から詰める）

- `write_idx` を使って `val` 以外の要素を左から順に詰める
- 順序を保つ・シンプル・安定した実装
- 時間計算量：O(n)、空間計算量：O(1)

---

### ✅ 解法2: two_pointers_swap.py（後ろからスワップ）

- `nums[left] == val` なら `nums[right]` と交換し `right` を減らす
- 順序は保持しないが操作回数が少なくて済む
- while ループで `left <= right` を制御
- 効率的な in-place 処理に強い

---

### ✅ 解法3: semi_optimized.py（オリジナルベース修正）

- `left`/`right` を進めながら中身をスワップ
- `left == right` のケースを含めて漏れなく処理
- 元のロジックをほぼ維持しつつ、安全性を高めた改良版

---

### ✅ 解法4: clear_fill_style.py（後ろに val を埋める）

- `val` 以外を前に詰め、残りを `val` で上書き
- 見た目が明確でデバッグしやすい
- LeetCode要件には不要だが、実務コードでは有効なケースあり

---

## ✅ 学び・気づき

- `val` 以外の要素数は `write_idx` もしくは `left` でカウントできるため、`for` ループで数え直す必要なし
- `val` の処理位置を変えることで順序保持/非保持の選択が可能
- `while left <= right:` の条件に注意。`left < right` では最後の1要素を処理し損ねる可能性がある
- LeetCodeの in-place 処理では「リストの後半はどうでもいい」が多い
