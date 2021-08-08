def valid_parenthesis(string):
    hashmap = {')': '(', ']': '[', '}': '{'}
    stack = []

    for ch in string:
        if ch in hashmap:
            if len(stack) < 1:
                return False
            if hashmap[ch] != stack.pop():
                return False
        else:
            stack.append(ch)

    return len(stack) == 0

print(valid_parenthesis("{{]}"))
        
            
