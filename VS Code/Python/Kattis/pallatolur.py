# Step 1: Read the input values for `a` and `b`
a = int(input().strip())
b = int(input().strip())

# Step 2: Identify if the range includes the number 2
even_primes = []
if a <= 2 <= b:
    even_primes.append(2)

# Step 3: Print the output
if even_primes:
    print(len(even_primes))
    print(' '.join(map(str, even_primes)))
else:
    print(':(')
