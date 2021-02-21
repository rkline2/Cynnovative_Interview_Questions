import re # using the sub() function

def get_Input():
    pal_input = input("Give me a word that you think is a palindrome: ")

    # removes punctuation and whitespace for comparing
    comp_input = pal_input.strip().lower().split()
    comp_input = ''.join(comp_input)
    comp_input = re.sub(r'[^\w\s]','',comp_input)

    return comp_input

def is_Pal(comp_input):
    return comp_input == comp_input[::-1]

def print_All_Palindromes(usr_input):
    FORMAT_LEN = 5 # the amount of "*" to display

    for x in range(0, len(usr_input)):
        print("\n{} stage {} {}".format( ("*" * FORMAT_LEN), (x + 1), ("*" * FORMAT_LEN) ))
        for y in range(x+1,len(usr_input) + 1):
            print("{} \t <{}>".format(usr_input[x:y], is_Pal(usr_input[x:y])).expandtabs(len(usr_input) + 2))
    print()

if __name__ == '__main__':
    comp_input = get_Input()
    print_All_Palindromes(comp_input)
    input("Enter any key to continue: ")
