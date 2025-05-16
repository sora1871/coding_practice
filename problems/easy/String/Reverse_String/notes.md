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

### ✅ v2_for_loop_swap.py  
- `for i in range(len(s))` を使いつつ、`j` を明示的に減らして2ポインタっぽく処理  
- `if i < j:` によって不要な後半のループでswapを防いでいる  
- 動作は正しいが、半分以降もループが続く点で若干の非効率

---

### ✅ v3_optimal_two_pointer.py  
- `while left < right:` を使った純粋なTwo Pointer法  
- `s[left], s[right] = s[right], s[left]` によりin-placeで反転  
- O(n) 時間・O(1) 空間の最適解  
- 最もPythonicかつ実務でも好まれるスタイル

---

## ✅ 学び・気づき

- Pythonの多重代入は一時タプルを使って安全にswapでき、in-placeとして扱われる  
- `s[::-1]` のような新しいリストを作る操作は in-place 要件を満たさない  
- 2ポインタ法（`left`と`right`で進む）は配列・文字列問題での基本パターン  
- `for`ループでも工夫次第で同様の処理は可能だが、`while`の方が直感的で最適な場合も多い
