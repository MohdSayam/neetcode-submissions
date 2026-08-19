class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ""
        for word in strs:
            length = len(word)
            new_str += f"{length}#{word}"
        return new_str

    def decode(self, s: str) -> List[str]:
        res = []
        
        # Keep going until the string is completely empty
        while s:
            # 1. Find the position of the very first '#'
            hashtag_index = s.find('#')
            
            # 2. Everything before the '#' is the length of the word
            length = int(s[:hashtag_index])
            
            # 3. Chop off the length number and the '#' from the front of 's'
            s = s[hashtag_index + 1:]
            
            # 4. Grab the exact word from the front of 's'
            word = s[:length]
            res.append(word)
            
            # 5. Chop off the word we just grabbed, leaving only the remaining string
            s = s[length:]
            
        return res




