# https://projecteuler.net/problem=71
# Farey Sequence: https://en.wikipedia.org/wiki/Farey_sequence

import time 
from fractions import Fraction

MAX_D = 1000000
TARGET = Fraction(3, 7)

# measure loop execution time - start time
start_time = time.perf_counter()

# Use the Farey sequence properties to find the fraction before 3/7
# For a fraction a/b, the mediant with c/d is (a+c)/(b+d)
# We'll use the fact that for consecutive Farey sequence terms a/b and c/d,
# the determinant bc-ad = 1

# Start with fractions that bracket our target 3/7
left = Fraction(2, 5)   # Left bracket (smaller than 3/7)
right = Fraction(3, 7)  # Right bracket (our target)

print(f"Starting with left={left}, right={right}")
count = 0

# Find the fraction with the largest denominator <= MAX_D that's less than 3/7
while True:
    count += 1
    # Calculate the mediant
    mediant = Fraction(left.numerator + right.numerator, 
                      left.denominator + right.denominator)
    print(f"Left: {left}. Right: {right}")
    
    # If the mediant's denominator is too large, we're done
    if mediant.denominator > MAX_D:
        result = left
        break
        
    # If the mediant is less than our target, it becomes our new left bracket
    if mediant < TARGET:
        left = mediant
    else:
        result = left

# measure execution time - end time
end_time = time.perf_counter()

# Print the results
print(f"Count of iterations: {count}")
print(f"Last fraction before 3/7: {result.numerator}/{result.denominator}")
print(f"Execution time: {end_time - start_time} seconds")