"""By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms, starting with 1 and 2 as seeds."""

# initizize upper limit
upper_lim = 4000000

# initialize seeds
two_before = 1
one_before = 2

seq = [two_before, one_before]

# initialize sum
even_sum = 2

n = 0

while n < upper_lim:
    next_val = two_before + one_before
    
    if next_val < upper_lim:
        seq.append(next_val)
    
        two_before = one_before
        one_before = next_val
    
        if next_val % 2 == 0:
            even_sum += next_val
            
        n = next_val
    
    else:
        break

print(seq)
print(even_sum)