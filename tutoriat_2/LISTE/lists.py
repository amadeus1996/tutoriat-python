sentence = "This is a short sentence"
digits   = "Today's date is 28/10/2024, 10:00 AM"
matrix   = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
nums1    = [4, 8, 15, 16]
nums2    = [1, 3, 4, 7, 1, 2, 0, 5, 3, 8, 2, 9, 0, 3, 1]
nums3    = [14, 150, 32, 188, 231, 29, 39120, 2849125, 582, 22222, 1482, 33132, 482, 19290, 10]
nums4    = [[1, 3, 2], [0, 5, 0, 0], [3], [1, 1, 1, 1, 1, 1], [2, 4, 1], [8], [8, 2]]
nums5    = [18, 512034, 142, 158, 321, 321042, 10]


# 1. Generate the even values in [n..0]
# n = int(input("n="))
n = 81
t = [x for x in range(n - 1 if n & 1 else n, -1, -2)]
print(t, end = "\n\n")


# 2. Sum of digits in a string
print(sum([int(digits[i]) for i in range(len(digits)) if digits[i].isdigit()]), end = "\n\n")


# 3. Square numbers from 1 to n
t = [x ** 2 for x in range(int(n ** (1 / 2)) + 1)]
print(t, end = "\n\n")


# 4. Remove vowels from every word in a sentence
t = " ".join(["".join([c for c in word if c not in "aeiouAEIOU"]) for word in sentence.split()])
print(t, end = "\n\n")


# 5. Delete duplicates
aux = nums2.copy() # CAREFUL "aux = nums2"!
i, n = 0, len(aux)
while i < n:
    if aux[i] in aux[:i]:
        del aux[i]
        n -= 1
    else:
        i += 1
print(aux, end = "\n\n")


# 6. Sort a list by the number of even digits
t = sorted(nums3, key = lambda x: len([c for c in str(x) if not(int(c) & 1)]))
print(t, end = "\n\n")


# 7. Return the missing number in [1..n]
t = [i for i in range(1, 26)] # numbers from 1 to 25
del t[14] # 15 is now missing

missing = 25 # missing = n
for i in range(len(t)):
    missing ^= (i + 1)
    missing ^= t[i]
print(missing, end = "\n\n")


# 8. Return the sum of the elements until the first 0.
print(sum(nums2[:nums2.index(0)]), end = "\n\n")


# 9. Find the 2nd largest element (duplicates allowed)
print(sorted(nums2)[-2], end = "\n\n")


# 10. Find all pairs that sum up to a target (don't repeat the same elements)
suma = 5
i, j = 0, len(nums2) - 1
nums2.sort()
while i != j:
    aux = nums2[i] + nums2[j]
    if aux < suma:
        i += 1
    elif aux > suma:
        j -= 1
    else:
        print(f"{nums2[i]}+{nums2[j]}={aux}", end = " ")
        i += 1
        j -= 1
print("\n")
# print([(nums2[i], nums2[j]) for i in range(len(nums2)) for j in range(i + 1, len(nums2)) if nums2[i] + nums2[j] == sum])


# 11. Circular permutations
print([nums1[i:] + nums1[:i] for i in range(len(nums1))], end = "\n\n")


# 12. Sum of odd digits for a number
x = 18027592
print(sum([int(c) for c in str(x) if int(c) & 1]), end = "\n\n")


# 13. Reverse sort a list of lists by the average of the numbers
t = sorted(nums4, key = lambda x: -(sum(x) / len(x)))
print(t, end = "\n\n")


# 14. Delete all the digits/numbers between the first two 0-digits in a list of numbers
nums5 = " ".join([str(x) for x in nums5])
try:
    index_1 = nums5.index("0")
    try:
        index_2 = nums5[(index_1 + 1):].index("0") + len(nums5[:index_1]) + 2
        print([int(x) for x in (nums5[:index_1] + " " + nums5[index_2:]).split()])
    except ValueError:
        print([int(x) for x in nums5.split()])
except ValueError:
    print([int(x) for x in nums5.split()])


# 15. Line swapping in a matrix - (i, i+1), (i+2, i+3), ...
n = len(matrix)
for i in range(1, n, 2):
    matrix[i], matrix[i - 1] = matrix[i - 1], matrix[i]
for line in matrix:
    print(*line)