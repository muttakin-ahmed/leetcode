def count_int_from_str(s):
    digit = ""
    sum = 0
    for i in range(len(s)):
        ch = s[i]
        if ch.isdigit():
            digit += ch
        elif digit:
            sum += int(digit)
            digit = ""
    return sum + int(digit) if digit else sum


print(count_int_from_str("go256sdfgd44"))

# Time complexity O(n)
# Space complexity O(1)
