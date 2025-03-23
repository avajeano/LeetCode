# time: O(n * m) | space: O(n)

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        res = []
        map = {}
        # groups 1, 2, 3
        arr = [
            "qwertyuiop",
            "assdfghjkl",
            "zxcvbnm"
        ]

        # initialize hashmap
        for i in range(len(arr)):
            for j in arr[i]:
                # naming the keyboard groups 1, 2, 3
                map[j] = i + 1
        
        for word in words:
            prev = 0
            valid = True
            saved_word = word
            word = word.lower()
        
            for letter in word:
                # checks for first letter of each word
                if prev == 0:
                    prev = map[letter]
                # all the other letters
                else:
                    if (prev != map[letter]):
                        valid = False
                        break
            if valid:
                res.append(saved_word)
        return res
