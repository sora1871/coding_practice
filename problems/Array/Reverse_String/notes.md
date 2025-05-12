# Reverse String  
問題リンク  
LeetCode #344 - [Reverse String](https://leetcode.com/problems/reverse-string/)

---

## 問題概要  
文字の配列 `s` が与えられる。in-placeで反転せよ。戻り値は不要で、`s` の中身を直接変更する。

例：  
入力: `["h","e","l","l","o"]`  
出力: `["o","l","l","e","h"]`

---

## ✅ 解法バリエーション

---

### ❌ v1_wrong_swap.py  
- `j = len(s)` としてしまい off-by-one エラー  
- `for` ループ内で `i += 1` を書いても無意味  
- `s[i], s[j] = s[j], s[i]` の実行前に `j` が配列外を参照してしまう可能性あり  
- 多重代入の効果やループ制御の基本に注意が必要

---

### ✅ v2_optimal_two_pointer.py  
- Two Pointer（`left`, `right`）を使い、左右から文字を交換して反転  
- Pythonの `s[left], s[right] = s[right], s[left]` は内部で一時的にタプルを作るが、in-place操作として扱われる  
- O(n) 時間・O(1) 空間の最適解

---

## ✅ 学び・気づき

- Pythonの多重代入は一時タプルを使って安全にswapでき、in-placeとして扱われる  
- `s[::-1]` のような新しいリストを作る操作は in-place 要件を満たさない  
- `while left < right:` のパターンは配列・文字列系の問題で頻出。Two Pointerの基本パターンとして覚えるべき
