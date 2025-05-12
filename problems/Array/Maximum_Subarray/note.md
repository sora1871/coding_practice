# Maximum Subarray  
問題リンク  
LeetCode #53 - [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

---

## 問題概要  
整数配列 `nums` が与えられる。連続する部分配列のうち、合計が最大になるものを見つけ、その合計値を返す。

例:  
`nums = [-2,1,-3,4,-1,2,1,-5,4]`  
→ 最大部分配列 `[4, -1, 2, 1]`（合計: `6`）

---

## ✅ 解法バリエーション

---

### ❌ brute_force.py  
- すべての (i, j) のペアを全探索して部分配列の和を比較  
- O(n²) 時間で非常に非効率  
- 小規模なデータでの動作確認・仕組み理解には向いている

---

### ❌ dp_mistake.py  
- DP配列を使って `dp[i] = max(nums[i], dp[0] + nums[i])` としたが、`dp[0]` 固定参照は誤り  
- 正しくは `dp[i-1]` を参照すべきだった  
- 遷移の理解はできているが、実装で文法ミス

---

### ✅ dp_correct.py  
- DP配列を使って `dp[i] = max(nums[i], dp[i-1] + nums[i])` を実装  
- 各位置で「その要素から再スタートするか、前の続きにするか」を選択  
- 最大値は `max(dp)` で管理  
- O(n) 時間・O(n) 空間

---

### ✅ optimal.py  
- Kadane’s Algorithm：DP配列を使わず、1変数で状態管理  
- `current_sum = max(num, current_sum + num)`  
- `max_sum` に最大値を随時更新  
- O(n) 時間・O(1) 空間の最適解  
- 実務や面接で最も好まれる形

---

## 🧪 ステップ実行例（Kadane's Algorithm）

```text
nums = [-2,1,-3,4,-1,2,1,-5,4]

current_sum: -2 → 1 → -2 → 4 → 3 → 5 → 6 → 1 → 5  
max_sum:    -2 → 1 → 1 → 4 → 4 → 5 → 6 → 6 → 6
→ 最終的な max_sum = 6（最大部分配列の合計）

✅ 学び・気づき
「部分配列を継続する価値があるか？」を逐次判断して状態を更新する

Kadane法は状態のリセットと継続を毎回選択する動的計画法（DP）の一種

Brute Force → DP → Kadane とステップを踏むことで理解が深まる