# Write a function that counts the occurrences of a substring in a string, case-sensitive.
# – Input: "hello world, hello", "hello"

def count_substring (s , sub ) :
    return s . count ( sub )
print ( count_substring ( " hello world , hello " , " hello " ) )
