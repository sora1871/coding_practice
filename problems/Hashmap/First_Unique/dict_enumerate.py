# ✅ 解法：2パスで出現回数をカウントし、最初のユニーク文字を探す
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}

        # 1回目：文字ごとの出現回数を記録
        for ch in s:
            count[ch] = count.get(ch, 0) + 1  # キーが無い場合は0として+1

        # 2回目：文字列を左から走査して、最初の"出現1回"の文字を探す
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx  # 条件を満たすインデックスを即返す

        return -1  # 該当する文字が存在しない場合

# 💡 意識したポイント：
# - dict.get() を使うことで KeyError を防ぎつつ簡潔に書ける
# - 文字列のインデックスを保持したいので enumerate を使用
# - 一意な文字がないケースも考慮して return -1 を用意
# - 空間計算量は O(1)：文字種は英小文字26種で固定
# - 時間計算量は O(n)：文字列の長さに比例する2回のループ
