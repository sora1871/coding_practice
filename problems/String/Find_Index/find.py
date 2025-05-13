# 組み込みの str.find() を使った実装
# 計算量: 平均 O(n) （内部的にC言語で最適化されている）
# 注意点:
#   - ライブラリ使用が許されているかを面接では確認すること
#   - needle が空文字列の場合も find() は正しく 0 を返す

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
