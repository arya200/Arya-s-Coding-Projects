# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “We have not given or received any unauthorized aid on this assignment”
#
# Names:          Arya Ramchandani 627007018
#
# Section:        021
# Assignment:     Lab07b - 1
# Date:           10 October 2018

print("This programs will convert the words you enter into pig latin words")
print("Please enter all words in lowercase")
print("")
# enters the list of words
words = []

stop = "stop"

# list that stores breaks up a word and stores each letter
list_check = []

# string to store the changed word
changing_word = ""

# string to store the first letter of the word
intermediate = ''

# input loop that stores all the words the user wants to convert

while True:

    individual_word = input("Enter a word you would like to convert to pig latin, enter 'stop' to receive the output : ")

    if(individual_word == stop):
        break
    else:
        words+=[individual_word]



for i in range(len(words)):

    #breaks up the word into it's constituent letters

    list_check = words[i]

    # checks if the first letter is a vowel

    if(list_check[0] == 'a' or list_check[0] == 'e' or list_check[0] == 'i'or list_check[0] == 'o'or list_check[0] == 'u'or list_check[0] == 'y' ):
        changing_word = words[i]

        changing_word += "yay"
        print(changing_word)

    # works if the word starts with a consonant

    else:
        latin = ""
        intermediate = list_check[0]
        for k in range(1,len(list_check)):
            latin += list_check[k]

        latin += intermediate + "ay"
        print(latin)

    # re sets the list with the broken up words to empty
    list_check = []




