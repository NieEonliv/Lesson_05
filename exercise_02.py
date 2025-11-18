inputString = input("Введить строку на английском языке: ")

vowels = { 'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0 }
vowelsKeys = vowels.keys()

for letter in inputString:
    if letter in vowelsKeys:
        vowels[letter] += 1

for key, value in vowels.items():
    print(f"{key}: {"false" if value == 0 else value}")