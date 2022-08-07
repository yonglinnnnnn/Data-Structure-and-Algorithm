# question 5
def num_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    # for each letter in text
    for i in range(len(text)):
        # check the word against each letter in vowels
        for u in range(0,5):
            if text[i] == vowels[u]:
                count += 1
    return count


print(num_vowels('data structure algorithm'))
