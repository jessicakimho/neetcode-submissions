class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
        # create a hashmap 
        # sort each word
        # if sorted(word) hasnt been seen, make it a key 
        # if it has been seen, add that word to the key's values
        # convert hashmap into a list and return its values

        seen = {}

        for word in strs:
            key = "".join(sorted(word))
            if key not in seen:
                seen[key] = []
            seen[key].append(word)
        return list(seen.values())