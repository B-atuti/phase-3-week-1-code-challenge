
import re
def highest_consonant_value(word):
    vowels = 'aeiou'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_word = re.sub('[aeiou]', '|', word.lower())
    word_list = new_word.split('|')
    char_value_list = []
    for chars in word_list:
        char_value = sum ([alphabet.find(char) +1 for char in chars])
        char_value_list.append(char_value)
    return f'Highest consonant value in {word} is {max(char_value_list)}'


while True:
    your_string = input("Enter a string: ")
    if your_string.isalpha():
        break
    else:
        print("Your Input Must Be A String With No Special Charaters And Spaces. ")

print(highest_consonant_value(your_string))

