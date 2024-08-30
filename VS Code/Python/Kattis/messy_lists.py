input()  # Read and discard the first line
wrong_lst = list(map(int, input().split()))  # Read the second line, split it, and convert to integers

# Create a sorted version of the list
right_list = sorted(wrong_lst)

# Count how many elements are out of order
counter = sum(1 for i in range(len(wrong_lst)) if wrong_lst[i] != right_list[i])

print(counter)
