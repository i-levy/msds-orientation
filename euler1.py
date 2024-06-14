"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6,
and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""

# initialize sum
sum = 0

# iterate through integers from 0 to 1000
for i in range(0,1000):
    # is the number divisible by 3 and 5?
    if i % 3 == 0 and i % 5 == 0:
        sum += i
    # is the number divisible only by 3?
    elif i % 3 == 0:
        sum += i
    # is the number divisible only by 3?
    elif i % 5 == 0:
        sum += i
print(sum)