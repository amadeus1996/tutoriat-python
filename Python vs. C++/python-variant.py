t = [122, 45, 111, 67, 321, 12, 8, 9, 100]
print(*sorted(t, key = lambda x: (len(set(str(x))), -x)))

t = "This, is   a test sentence?!..."
print('-'.join((word.strip(" .,?!")[::-1] if len(word) > 2 else word.strip(" .,!?") for word in t.split())))


