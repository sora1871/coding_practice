# FizzBuzz

##  問題リンク
[LeetCode #412 - Fizz Buzz](https://leetcode.com/problems/fizz-buzz/)

---

##  問題概要

1 から `n` までの整数を出力する。以下のルールに従って、文字列のリストを返す：

- 3の倍数 → "Fizz"
- 5の倍数 → "Buzz"
- 15の倍数 → "FizzBuzz"
- それ以外 → 数字をそのまま文字列で

---

## ✅ 解法（基本的な条件分岐）

### fizzbuzz.py
- `range(1, n + 1)` でループ（1〜n）
- `if → elif → elif → else` で排他的に判定
- `% 15` を先にチェックしないと `"Fizz"` + `"Buzz"` が両方追加されるバグに

---

## ✅ 学び・気づき

- 条件分岐の順序はロジックの正確性に直結する（Fizz → Buzz → FizzBuzzはNG）
- `List[str]` を返すために `str(i)` の使い方を理解しておくと便利
- 単純だが、Python の基本構文を確認するには非常に良い問題

---
