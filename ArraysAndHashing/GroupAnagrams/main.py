from typing import List
# How should we handle this?
# Should be related to the original anagram problem.
# Instead, we might can sort the string
#
#

class GroupAnagram:
    def solution(strs: List[str]) -> List[List[str]]:
        # How should we handle this?
        # Should be related to the anagram problem.
        # Have hashmap of lists
        # Sort and check if the sorted word is stored as a key
        # Append if not, if it does, add it to the list for the matching key

        anagram_map = {}
        result = []

        for word in strs:
            s_word = "".join(sorted(word))
            if s_word in anagram_map:
                anagram_map[s_word].append(word)
            else:
                anagram_map[s_word] = [word]

        for val in anagram_map.values():
            result.append(val)

        return result
