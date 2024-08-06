class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Count of characters in both the strings are same even though they appear in a random order

        #Check if the lengths of the strings are not equal . If the lengths are not equal then they are not anagrams to each other => BASE CASE

        if len(s) != len(t):
            return False 

        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        return countS == countT

  #PATTERN: Count any value in a string use a hashmap as it has a key value store to store the values and compare and we can iterate through the hashmap

  #TC : O(N)
  #SC : O(N)
