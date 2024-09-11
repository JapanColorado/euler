previous = 1
current = 2
limit = 4*(10**6)

total = 0

while current < limit:
    # Check if current term is even
    if current % 2 == 0:
        sum += current
    
    # Generate next integer #! My Approach:!#
    # previous = int(current - previous)
    # current += previous

    # Better solution:
    previous, current = current, previous+current

print(total)