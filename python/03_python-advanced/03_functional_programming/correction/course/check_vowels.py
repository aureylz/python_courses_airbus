def check_vowels(letter):
  list_of_vowels = ['a', 'e', 'i', 'o', 'u','y']
  if letter in list_of_vowels:
      return True
  else:
      return False
letters = ['t', 'e', 'm', 'c', 'i', 'd', 'z', 'p', 'o']
filtered_object = filter(check_vowels, letters)
print(list(filtered_object))