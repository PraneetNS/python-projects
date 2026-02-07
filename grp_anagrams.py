from collections import defaultdict
class Solution:
    def groupAnagrams(list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            anagrams[key].append(s)
        return list(anagrams.values())