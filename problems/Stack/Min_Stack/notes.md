# Min Stack

## 問題概要

LeetCode - Min Stack:  
https://leetcode.com/problems/min-stack/description/

特殊なスタック MinStack を実装する。すべての操作 (push, pop, top, getMin) を O(1) 時間で行うことが条件。

---

## 解法の30文字概要

スタック + 最小値スタックを両方管理

---

## 解法のアイデア

- 通常の stack に加えて、"min_stack" を利用
- `push` のたびに現在の最小値を min_stack に保存
- `pop` は両方から pop
- `getMin` は min_stack の最後を取るだけで、当然 O(1)

---

## 学び・気づき

- O(1) で min を取るには、別のスタックで最小値をいつも管理する必要がある
- pop するときは、stack と min_stack を同時に pop すれば統合が取れる
- 同じ最小値が連続して push されても定常時間で処理可
- `self.` はクラスのメンバにアクセスするために必要
- Python の `__init__.py` はパッケージ化に必要

---

## テスト例

```python
minStack = MinStack()
minStack.push(3)         # stack: [3], min_stack: [3]
minStack.push(5)         # stack: [3,5], min_stack: [3,3]
minStack.getMin()        # => 3
minStack.push(2)         # stack: [3,5,2], min_stack: [3,3,2]
minStack.push(1)         # stack: [3,5,2,1], min_stack: [3,3,2,1]
minStack.getMin()        # => 1
minStack.pop()           # => stack: [3,5,2], min_stack: [3,3,2]
minStack.getMin()        # => 2
minStack.top()           # => 2
