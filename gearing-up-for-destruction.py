# Gearing Up for Destruction
# ==========================

# As Commander Lambda's personal assistant, you've been assigned the task of configuring the LAMBCHOP doomsday device's axial orientation gears. It should be pretty simple -- just add gears to create the appropriate rotation ratio. But the problem is, due to the layout of the LAMBCHOP and the complicated system of beams and pipes supporting it, the pegs that will support the gears are fixed in place.

# The LAMBCHOP's engineers have given you lists identifying the placement of groups of pegs along various support beams. You need to place a gear on each peg (otherwise the gears will collide with unoccupied pegs). The engineers have plenty of gears in all different sizes stocked up, so you can choose gears of any size, from a radius of 1 on up. Your goal is to build a system where the last gear rotates at twice the rate (in revolutions per minute, or rpm) of the first gear, no matter the direction. Each gear (except the last) touches and turns the gear on the next peg to the right.

# Given a list of distinct positive integers named pegs representing the location of each peg along the support beam, write a function solution(pegs) which, if there is a solution, returns a list of two positive integers a and b representing the numerator and denominator of the first gear's radius in its simplest form in order to achieve the goal above, such that radius = a/b. The ratio a/b should be greater than or equal to 1. Not all support configurations will necessarily be capable of creating the proper rotation ratio, so if the task is impossible, the function solution(pegs) should return the list [-1, -1].

# For example, if the pegs are placed at [4, 30, 50], then the first gear could have a radius of 12, the second gear could have a radius of 14, and the last one a radius of 6. Thus, the last gear would rotate twice as fast as the first one. In this case, pegs would be [4, 30, 50] and solution(pegs) should return [12, 1].

# The list pegs will be given sorted in ascending order and will contain at least 2 and no more than 20 distinct positive integers, all between 1 and 10000 inclusive.

# Languages
# =========

# To provide a Java solution, edit Solution.java
# To provide a Python solution, edit solution.py

# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Python cases --
# Input:
# solution.solution([4, 30, 50])
# Output:
#     12,1

# Input:
# solution.solution([4, 17, 50])
# Output:
#     -1,-1

# Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

# ===================================================

# https://en.wikipedia.org/wiki/Gear_train

# Speed of Gear System:
    # r_0 * w_0 = r_n * w_n, where:
    # r = radius
    # w = angular velocity
    # n = number of gears

    # Therefore:
        # r_0 = (w_n/w_0) * r_n
        # => r_0 = 2 * r_n

# Space Between Gears:
    # r_1 + r_2 = s_1
    # r_2 + r_3 = s_2

    # Therefore:
        # r_1 - r_3 = s_1 - s_2

# Example Case:
    # n = number of gears
    # Pn = reference point of peg n
    # r_n = radius

    # n = 0:
        # Impossible, return [-1,-1]

    # n = 1:
        # Impossible, return [-1,-1]

    # n = 2:
        # r_0 + r_1 = P1 - PO
        # r_0 = 2 * r_1 => r_1 = r_0 / 2

        # Simplifying:
            # => r_0 + (r_0 / 2) = P1 - P0
            # => 2r_0 + r_0 = 2(P1 - P0)
            # => 3r_0 = 2(P1 - P0)
            # => r_0 = (2 / 3) * (-P0 + P1)

    # n = 3:
        # r_0 + r_1 = P1 - P0
        # r_1 + r_2 = P2 - P1
        # r_0 = 2 * r_2 => r_2 = r_0 / 2

        # Simplifying:
            # =>(r_0 + r_1) - (r_1 + r_2) = (P1 - P0) - (P2 - P1)
            # => r_0 - r2 = -P0 + 2P1 - P2
            # => r_0 - (r_0 / 2) = -P0 + 2P1 - P2
            # => 2r_0 - r_0 = 2(-P0 + 2P1 - P2)
            # => r_0 = 2(-P0 + 2P1 - P2)

    # n = 4:
        # r_0 + r_1 = P1 - P0
        # r_1 + r_2 = P2 - P1
        # r_2 + r_3 = P3 - P2
        # r_ 0 = 2 * r_3 => r_3 = r_0 / 2

        # Simplifying:
            # =>(r_0 + r_1) - (r_1 + r_2) + (r_2 + r_3) = (P1 - P0) - (P2 - P1) + (P3 - P2)
            # => r_0 + r_3 = -P0 + 2P1 - 2P2 + P3
            # => r_0 + (r_0 / 2) = -P0 + 2P1 - 2P2 + P3
            # => 2r_0 + r_0 = 2(-P0 + 2P1 - 2P2 + P3)
            # => 3r_0 = 2(-P0 + 2P1 - 2P2 + P3)
            # => r_0 = (2 / 3) * (-P0 + 2P1 - 2P2 + P3)

    # n = 5:
        # r_0 + r_1 = P1 - P0
        # r_1 + r_2 = P2 - P1
        # r_2 + r_3 = P3 - P2
        # r_3 + r_4 = P4 - P3
        # r_ 0 = 2 * r_4 => r_4 = r_0 / 2

        # Simplifying:
         # =>(r_0 + r_1) - (r_1 + r_2) + (r_2 + r_3) - (r_3 + r_4) = (P1 - P0) - (P2 - P1) + (P3 - P2) - (P4 - P3)
         # => r_0 - r_4 = -P0 + 2P1 - 2P2 + 2P3 - P4
         # => r_0 - (r_0 / 2) = -P0 + 2P1 - 2P2 + 2P3 - P4
         # => 2r_0 - r_0 = 2(-P0 + 2P1 - 2P2 + 2P3 - P4)
         # => r_0 = = 2(-P0 + 2P1 - 2P2 + 2P3 - P4)

# Formula:
    # If n is odd,  r_0 = 2 * (Sum(Odd_Indexes) - Sum(Even_Indexes))
    # If n is even, r_0 = (2 / 3) * (Sum(Odd_Indexes) - Sum(Even_Indexes))

from fractions import Fraction

def solution(pegs):
    arr_length = len(pegs)

    if (not pegs) or (arr_length == 1):
        return [-1, -1]

    total = 0
    # Even number of pegs
    if arr_length % 2 == 0:
        total = (-pegs[0] + pegs[arr_length - 1])
    # Odd number of pegs
    elif arr_length % 2 == 1:
        total = (-pegs[0] - pegs[arr_length - 1])

    if arr_length > 2:
        for i in range (1, arr_length - 1):
            if i % 2 == 0: # Even index
                total += -2 * pegs[i]
            elif i % 2 == 1: # Odd index
                total += 2 * pegs[i]

    first_gear_radius = 0
    if arr_length % 2 == 0:
        first_gear_radius = 2 * Fraction(float(total)/3).limit_denominator()
    elif arr_length % 2 == 1:
        first_gear_radius = 2 * Fraction(total).limit_denominator()

    # Check the input array of pegs to verify that the pegs radius is atleast 1.
        # last_gear_radius >= 1 and first_gear_radius = 2 * last_gear_radius
        # => first_gear_radius >= 2

    if first_gear_radius < 2:
        return [-1, -1]

    current_gear_radius = first_gear_radius
    for i in range (0, arr_length - 1):
        current_distance = pegs[i + 1] - pegs[i]
        next_gear_radius = current_distance - current_gear_radius
        if (current_gear_radius < 1) or (next_gear_radius < 1):
            return [-1, -1]
        else:
            current_gear_radius = next_gear_radius

    return [first_gear_radius.numerator , first_gear_radius.denominator]


print(solution([4, 30, 50]))
# Correct Answer: 12,1
print(solution([4, 17, 50]))
# Correct Answer:-1,-1
