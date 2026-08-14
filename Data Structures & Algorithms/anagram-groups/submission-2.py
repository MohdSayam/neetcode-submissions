from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Creating a hash map where the key is the sorted word and value is the list of anagrams 
        anagram_map = defaultdict(list)

        for s in strs:
            # here i am sorting each word e.g sort "cat" = ["a", "c", "t"] and by joing it it will be again "act"
            sorted_key = "".join(sorted(s))

            # append the original string to the matching key's list
            anagram_map[sorted_key].append(s)

        return list(anagram_map.values())

            




        