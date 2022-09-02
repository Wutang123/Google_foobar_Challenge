# Braille Translation
# ===================

# Because Commander Lambda is an equal-opportunity despot, they have several visually-impaired minions. But Lambda never bothered to follow intergalactic standards for workplace accommodations, so those minions have a hard time navigating her space station. You figure printing out Braille signs will help them, and -- since you'll be promoting efficiency at the same time -- increase your chances of a promotion.

# Braille is a writing system used to read by touch instead of by sight. Each character is composed of 6 dots in a 2x3 grid, where each dot can either be a bump or be flat (no bump). You plan to translate the signs around the space station to Braille so that the minions under Commander Lambda's command can feel the bumps on the signs and "read" the text with their touch. The special printer which can print the bumps onto the signs expects the dots in the following order:
# 1 4
# 2 5
# 3 6

# So given the plain text word "code", you get the Braille dots:

# 11 10 11 10
# 00 01 01 01
# 00 10 00 00

# where 1 represents a bump and 0 represents no bump.  Put together, "code" becomes the output string "100100101010100110100010".

# Write a function solution(plaintext) that takes a string parameter and returns a string of 1's and 0's representing the bumps and absence of bumps in the input string. Your function should be able to encode the 26 lowercase letters, handle capital letters by adding a Braille capitalization mark before that character, and use a blank character (000000) for spaces. All signs on the space station are less than fifty characters long and use only letters and spaces.

# Languages
# =========

# To provide a Python solution, edit solution.py
# To provide a Java solution, edit Solution.java

# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Python cases --
# Input:
# solution.solution("code")
# Output:
#     100100101010100110100010

# Input:
# solution.solution("Braille")
# Output:
#     000001110000111010100000010100111000111000100010

# Input:
# solution.solution("The quick brown fox jumps over the lazy dog")
# Output:
#     000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110

# Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

def solution(s):

    binary_dict = {
        "space"   : "000000",
        "capital" : "000001",
        1  : "100000",
        2  : "110000",
        3  : "100100",
        4  : "100110",
        5  : "100010",
        6  : "110100",
        7  : "110110",
        8  : "110010",
        9  : "010100",
        10 : "010110",
        11 : "101000",
        12 : "111000",
        13 : "101100",
        14 : "101110",
        15 : "101010",
        16 : "111100",
        17 : "111110",
        18 : "111010",
        19 : "011100",
        20 : "011110",
        21 : "101001",
        22 : "111001",
        23 : "010111",
        24 : "101101",
        25 : "101111",
        26 : "101011",
        }

    binary_ret = []
    s = list(s)

    for i in range(0, len(s)):
        if ord(s[i]) == 32:
            binary_ret.append(binary_dict["space"])
            continue
        if ord(s[i]) >= 65 and ord(s[i]) <= 90:
            binary_ret.append(binary_dict["capital"])

        binary_ret.append(binary_dict[ord( s[i].lower() ) - ord("a") + 1])

    string_binary_ret = "".join(binary_ret)
    return string_binary_ret

print(solution("code"))
# Correct Output: 000001110000111010100000010100111000111000100010
print(solution("Braille"))
# Correct Output: 000001110000111010100000010100111000111000100010
print(solution("The quick brown fox jumps over the lazy dog")
# Correct Output: 000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110