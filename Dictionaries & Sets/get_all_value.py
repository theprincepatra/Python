def extract_value(data, delimiter):
    input = [i.split(delimiter)[1].strip() for i in data if delimiter in i]
    return input

dataset = ["Name: Alice", "Age: 30", "City: New York", "Invalid"]
delimiter = ":"
extracted = extract_value(dataset, delimiter)
print(extracted)

# output:
# ['Alice', '30', 'New York']
