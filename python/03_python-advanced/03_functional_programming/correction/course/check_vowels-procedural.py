list_of_vowels = ["a", "e", "i", "o", "u", "y"]
filtered_object = []
for item in letters:
    if item in list_of_vowels:
        filtered_object.append(item)
print(filtered_object)
