# Valid Palindrome

##  問題リンク
[Valid Palindrome – LeetCode #125](https://leetcode.com/problems/valid-palindrome/)

---

## 問題概要

与えられた文字列 `s` に対して、  
- **英数字のみを対象**
- **大文字小文字は区別しない**  
という条件で、**前から読んでも後ろから読んでも同じ＝回文かどうか**を判定する。

---

##  解法一覧

### ❌ v1_missing_isalnum_parens.py
- `.isalnum` に `()` をつけ忘れたことで、関数として呼び出せておらずバグ
- `s[left].isalnum` → `s[left].isalnum()` が正解

### ❌ v2_no_filter.py
- 記号や空白、句読点などの「非英数字」もそのまま比較してしまい、誤判定になる
- 「空白」「カンマ」などを除外する処理が必要だった

### ✅ optimal.py
- 2ポインタを使い、左右から英数字のみを比較
- `.isalnum()` でフィルタ、`.lower()` で大文字小文字を無視
- 文字列を前処理せずにそのまま走査する効率的な実装

---

##  学び・気づき

- Pythonでは文字列に `s[i]` でアクセスできる（リストと同じ）
- 関数を呼び出すときは **`()` を忘れない**！（超重要）
- `.isalnum()` は英数字のみTrueになる便利な組み込み関数
- 境界条件をチェックするには `while left < right and ...` のように **複数条件を安全に組み合わせる**

---

##  テストケース例

```python
assert Solution().isPalindrome("A man, a plan, a canal: Panama") == True
assert Solution().isPalindrome("race a car") == False
assert Solution().isPalindrome(" ") == True
assert Solution().isPalindrome("No lemon, no melon") == True
