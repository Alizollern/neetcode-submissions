class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_text = str()
        for string in strs:
            encode_text += str(len(string)) + "#"+ string
        return encode_text

    def decode(self, s: str) -> List[str]:
        counter_i  = 0
        word_list = list()
        while counter_i < len(s):
            counter_j = counter_i
            while s[counter_j] != '#' : counter_j += 1
            length = int(s[counter_i:counter_j])
            word = s[counter_j + 1 : counter_j + 1 + length]
            word_list.append(word)
            counter_i = counter_j + 1 + length
        return word_list





