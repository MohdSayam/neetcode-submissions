class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = dict()
        hash_t = dict()
        flag = True

        if len(s) != len(t):
            return False
        
        for i in s:
            if i not in hash_s:
                hash_s[i] = 1 
            else: 
                hash_s[i] += 1
            
        for i in t:
            if i not in hash_t:
                hash_t[i] = 1 
            else: 
                hash_t[i] += 1
        
        print(hash_s, hash_t)

        for i in hash_s:
            if i not in hash_t:
                return False
            
            if hash_t[i] != hash_s[i]:
                return False

        return flag

        