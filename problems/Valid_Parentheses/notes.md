# Valid Parentheses

## 🔗 問題リンク
[Valid Parentheses – LeetCode #20](https://leetcode.com/problems/valid-parentheses/)

---

## 🧠 問題概要

与えられた文字列 `s` に含まれる括弧 `()[]{}` が、すべて正しく対応しているかを判定する。  
- 開き括弧には必ず閉じ括弧が対応していること  
- 括弧の順序も正しい必要がある

---

## ✅ 解法バリエーション

### ❌ v1_logic_misuse.py
- 条件式の構文ミス：`if char == "(" or "[" or "{"` は常にTrueになる
- 本来は `if char in "([{":` のように書くべき
- このような論理ミスは非常に起きやすいので注意

---

### ✅ optimal.py（閉じ → 開きペア）
- 対応ペアを `pairs = {")": "(", ...}` のように定義
- `stack.pop()` が `pairs[char]` と一致するかをチェック
- `pop()` 前に `not stack` で空チェック（短絡評価）も完璧

---

### ✅ v2_reverse_pairs.py（開き → 閉じペア）
- 開き括弧が出たとき、対応する閉じ括弧を `stack` に積む
- 閉じ括弧が来たとき、`stack.pop()` が `char` と一致するかを確認
- より前向きな構造で、コードの見やすさはこちらが好みという人も多い

---

## ✅ 学び・気づき

- Pythonの `or` は **短絡評価**（左がTrueなら右は評価されない）なので、`if not stack or stack.pop() != ...` は安全な書き方
- スタックは `list` で実装できる（`append`, `pop`）
- ペアの辞書はどちら向きでもいいが、**ロジックを合わせることが重要**
- `stack[-1]` で確認する方法 or `stack.pop()` を比較に使う方法がある
- `not stack` は「スタックが空か？」を確認するシンプルな方法

---
