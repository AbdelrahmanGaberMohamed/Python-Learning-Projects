def find_occurrences(text, pattern):
    # Write your code here
    count = 0
    result = []
    index = []
    if pattern not in text:
        result = [False, 0, []]
        return tuple(result)
    else:
        result.append(True)

        for i in range(len(text)):
            if len(text) - i < len(pattern):
                break
            sub_count = 0 
            for j in range(len(pattern)):
                if pattern[j] == text[i+j]:
                    sub_count += 1
                else:
                    break
            if sub_count == len(pattern):
                count += 1
                index.append(i)
        result.append(count)
        result.append(index)
        return tuple(result)


# Read input
text = input()
pattern = input()

# Call your function and print the result
result = find_occurrences(text, pattern)
print(result)