# Positional arguments v.s named arguments

def multiply(x, y):
    result = x * y
    return result


def is_palindrome(string):
    string = string.lower()
    r_string = string[::-1]
    if(r_string == string):
        return True
    else:
        return False

def is_palindrome_sentence(string):
    sentence = ""
    for letter in string:
        if letter.isalnum() and not letter.isspace():
            sentence += letter

    print(sentence)
    return is_palindrome(sentence)

while(True):

    word = input("Please enter a word to see if it's a Palindrome: ")

    if (is_palindrome_sentence(word)):
        print("'{}' is a palindrome!".format(word))
    else:
        print("'{}' is not a palindrome".format(word))
