def count_int_from_str(s):
    digit = ""
    sum = 0
    # Traversing each character in the string
    for i in range(len(s)):
        ch = s[i]
        # If the char is a digit
        if ch.isdigit():
            # Appedning the char to the str digit
            digit += ch
        # Once the number is finished
        elif digit:
            # We are putting current sum in the variable sum
            sum += int(digit)
            # And then we are going to reset the variable digit
            digit = ""
    # Finally, we will return current sum + digit if digit is not empty
    # Otherwise we return sum
    return sum + int(digit) if digit else sum


print(count_int_from_str("go256sdfgd444m4"))

# Time complexity O(n)
# Space complexity O(1)
