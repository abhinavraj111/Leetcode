class Solution:
    def mergeAlternately(self, word1, word2):
        merged_string = []
        i, j = 0, 0
        len1, len2 = len(word1), len(word2)

        # Iterate over both strings and merge them
        while i < len1 or j < len2:
            if i < len1:
                merged_string.append(word1[i])
                i += 1
            if j < len2:
                merged_string.append(word2[j])
                j += 1
        
        return ''.join(merged_string)

