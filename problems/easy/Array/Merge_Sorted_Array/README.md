# Merge Sorted Array

## 問題概要
2つのソート済み配列 `nums1` と `nums2` をマージする。`nums1` にはあらかじめ `m + n` のサイズがあり、前半 `m` 要素が有効データ、後半 `n` 要素が0で埋まっている。

`nums2` の全要素を `nums1` にマージし、1つの昇順ソート済み配列を `nums1` に直接上書きで格納せよ。

## 解法：2ポインターによる末尾からのマージ（最適解）

### アプローチ
- `nums1` の末尾には空き領域があることを活用
- 大きい要素から後ろに埋めていくことで、in-place に処理可能
- ポインター `i`（nums1 実データの末尾）、`j`（nums2の末尾）、`k`（nums1の全体末尾）を使う

### 実装のポイント
- 比較は `nums1[i] >= nums2[j]` のようにして、大きい方を `nums1[k]` に格納
- `j` 側が残っている場合のみループを回して補完
- `nums1` 側の要素はすでに正しい位置にあるため、補完不要

### 計算量
- 時間計算量：O(m + n)
- 空間計算量：O(1)

## 学び・気づき
- in-place 処理は**後ろから**行うと上書きが発生しない
- ポインター操作で条件をミスるとバグになりやすいので注意
- `nums1` の初期状態がしっかり仮定通りになっていることを前提にしている

## 参考コード
`merge_sorted_array_optimal.py` を参照
