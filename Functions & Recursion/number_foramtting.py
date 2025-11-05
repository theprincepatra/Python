# Write a function that takes a string containing a phone number in various formats and formats it as "123-456-7890".
# Return "Invalid" if the input is not a valid 10-digit phone number.

def format_phone_number(s):
    digits = "".join(char for char in s if char.isdigit())
    if len(digits) != 10:
        return "Invalid"
    # Format as XXX-XXX-XXXX
    return (f"{digits[:3]}-{digits[3:6]}-{digits[6:]}")

print(format_phone_number("(123) 456-7890"))
print(format_phone_number("123456789"))

# output:
# 123-456-7890
# Invalid
