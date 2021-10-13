def Find_substring_and_return_index(self, haystack: str, needle: str) -> int:
        # If the needle is an empty string -> return 0
        if needle == "":
            return 0
        
        # We are now finding the needle in the haystack
        # Algorithm: traverse the haystack
        for i in range(len(haystack)):
            # For each letter, check that haystack[current:current+len(needle)] == needle or not
            # If yes -> found the needle and return current
            if haystack[i:i+len(needle)] == needle:
                return i
        # Needle could not be found
        return -1
      
# Runtime complexity: O(n), where n = len(haystack)
# Space complexity: O(1), as we are not initiating any extra variable
