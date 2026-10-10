class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(i)}#{i}" for i in strs)

    def decode(self, s: str) -> List[str]:
        x = 0
        l_result = []
        while x < len(s):
            delimiter_idx = s.find('#', x)
            length = int(s[x:delimiter_idx])
            my_str = s[delimiter_idx + 1: delimiter_idx + 1 + length]
            l_result.append(my_str)
            x = delimiter_idx + 1 + length
        return l_result
