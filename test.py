numbers = [-45, 30, 14, -1]

maxpositive = abs(max(numbers))
minnegative = abs(min(numbers))

if maxpositive > minnegative:
    print(max(numbers))
else:
    print(min(numbers))