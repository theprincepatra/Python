# Write a function that compresses a string by replacing repeated characters with the character followed by the count of repetitions.
# If the compressed string is not shorter, return the original string.
# – Input: "aabcccccaaa

def compress_string ( s ) :
    if not s :
        return s
    compressed = []
    count = 1
    current = s[0]
    for char in s[1:]:
        if char == current:
            count += 1
        else:
            compressed.append(current + str(count))
            current = char
            count = 1
    compressed.append(current + str(count))
    result = "".join(compressed)
    return result if len(result) < len(s) else s

print(compress_string("aabcccccaaa"))
