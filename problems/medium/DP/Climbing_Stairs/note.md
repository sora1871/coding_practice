# Climbing Stairs

## 問題概要

階段を上るとき、1段または2段ずつ登ることができる。  
段数 `n` が与えられたとき、頂上にたどり着くための異なる方法の総数を求める。

---

## 解法①：動的計画法（DP使用）

- `dp[i] = dp[i-1] + dp[i-2]`（フィボナッチ数列と同じ）
- 初期条件：`dp[1] = 1`, `dp[2] = 2`
- 配列で状態を持つので実装が明快
- 時間計算量：O(n)、空間計算量：O(n)

---

## 解法②：定数空間でのDP最適化

- 直近2つの状態（a, b）だけで遷移可能
- 配列を使わず省メモリ
- 時間計算量：O(n)、空間計算量：O(1)

---

## 学び・気づき

- フィボナッチ的構造に気づけるかがカギ
- `dp`配列は必須ではなく、直前2値だけで十分
- 再帰は指数時間になるため非推奨
- Pythonの `a, b = b, a + b` 構文は簡潔かつ効率的

---
