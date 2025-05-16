# Longest Substring Without Repeating Characters

## 問題リンク
[Longest Substring Without Repeating Characters – LeetCode #3](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

---

## ✅ 解法バリエーション

### ✅ brute_force.py
- 全ての開始点 `i` に対して、そこから重複のない文字を1つずつセットで追跡
- 重複が出たら break、最大長を記録
- 時間計算量：O(n²)、空間計算量：O(n)
- 小さいケースでは動作確認に便利だが、大きな入力ではTLEする可能性大

---

### ✅ using_set.py
- スライディングウィンドウ方式で、セットを用いて重複文字を管理
- 右端 `right` を進めつつ、`while` ループで左端 `left` を縮めて重複を排除
- 可読性が高く、動作も直感的
- 時間計算量：O(n)、空間計算量：O(n)

---

### ✅ using_hashmap.py
- スライディングウィンドウ + ハッシュマップを用いた最適解
- 文字がすでにウィンドウ内にあれば、`left` をその次のインデックスに一気に更新
- 辞書で出現位置を記録することで高速にスキップが可能
- 時間計算量：O(n)、空間計算量：O(min(n, m))

---

## ✅ 最終比較と流れ

| バージョン             | 計算量   | 特徴                                      |
|------------------------|----------|-------------------------------------------|
| ✅ brute_force.py      | O(n²)     | 全探索、理解はしやすいが非効率             |
| ✅ using_set.py        | O(n)      | セットベース、直感的で安定                 |
| ✅ using_hashmap.py    | O(n)      | 最適。重複時に一気にスキップ               |

---

## ✅ 学び

- **スライディングウィンドウ + 辞書/セット** のパターンは頻出
- `if s[i] in dict` の条件と同時に `dict[s[i]] >= left` の条件も忘れずに
- 「辞書のキーには in が使えるが、値で検索したいときは dict.values() が必要」
- 重複回避のロジックとして `left` を更新する位置に注意する
