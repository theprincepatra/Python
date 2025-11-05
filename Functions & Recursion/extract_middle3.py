# Write a function that extracts the middle three characters of a string. If the string length is even or less than 3, return the string itself.
def middle_three ( s ) :
    if len ( s ) < 3 or len ( s ) % 2 == 0:
        return s
    mid = len ( s ) // 2
    return s [ mid -1: mid +2]
print (middle_three("Python"))
print (middle_three("Aryan"))
