class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        counter = 0
        attr_id = 0
        attrs = ['type', 'color', 'name']
        for i in range(len(attrs)):
            if attrs[i] == ruleKey:
                attr_id = i
        
        for item in items:
            if item[attr_id] == ruleValue:
                counter += 1
                
        return counter
      
# Runtime complexity: O(n), where n = len(items) because the list is being iterated just once.
# Space complexity: O(n) as there is one list being initiated and used in the code body, plus there are 2 other variables.
