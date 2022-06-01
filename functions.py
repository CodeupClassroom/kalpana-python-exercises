
# Only run the following code if I specifically run the script from the terminal
if __name__ == '__main__':
    # Setting up manual tests
    user_number1 = int(input("Please input a number"))
    user_number2 = int(input("Please input another number"))

    print(f"{user_number1} * {user_number2} is {multiply(user_number1, user_number2)}")

    print("Thanks for running my code!")

    # More automated tests
    assert add(2, 3) == 5
    assert multiply(2, 3) == 6
    print("Automated tests ran appropriately")



# Exercise 1
# Define a function named is_two. 
# It should accept one input and return True if 
# the passed input is either the number or the string 2, 
# False otherwise.

def is_two(n):
    return n == 2 or n == '2'

# Exercise 2
# Define a function named is_vowel. 
# It should return True if the passed string is a vowel, 
# False otherwise.

def is_vowel(string):
    return len(string) == 1 and string.lower() in 'aeiou'

# Exercise 3
# Define a function named is_consonant.
# It should return True if the passed string is a consonant, 
# False otherwise. Use your is_vowel function to accomplish this.


def is_consonant(string):
    return len(string) == 1 and not is_vowel(string) and string.isalpha()

# Exercise 4
# Define a function that accepts a string that is a word. 
# The function should capitalize the 
# first letter of the word if the word starts with a consonant.

def capitalize_starting_consonant(string):
    if type(string) != str:
        return False
    first_letter = string[0]
    if is_consonant(first_letter):
        string = string.capitalize()
    return string

# Exercise 5
# Define a function named calculate_tip. 
# It should accept a tip percentage 
# (a number between 0 and 1) and the bill total, 
# and return the amount to tip.

def calculate_tip(tip_percentage, bill):
    amount_to_tip = bill * tip_percentage
    return amount_to_tip


# Exercise 6
# Define a function named apply_discount. 
# It should accept a original price, and a discount percentage, 
# and return the price after the discount is applied.

def apply_discount(price, discount_percentage):
    discount = price * discount_percentage
    return price - discount


# Exercise 7
# Define a function named handle_commas. 
# It should accept a string that is a number that contains 
# commas in it as input, 
# and return a number as output.

def handle_commas(numeric_string):
    string_without_commas = numeric_string.replace(',', '')
    actual_number = int(string_without_commas)
    return actual_number

# Exercise 8
# Define a function named get_letter_grade. 
# It should accept a number and return the letter grade 
# associated with that number (A-F).

def get_letter_grade(grade):
    if type(grade) == int or type(grade) == float:
        if grade >= 90:
            return "A"
        elif grade >= 80:
            return "B"
        elif grade >= 70:
            return "C"
        elif grade >= 60:
            return "D"
        else:
            return "F"
    else:
        return "Input must be a number"

# Exercise 9
# Define a function named remove_vowels that accepts a 
# string and returns a string with all the vowels removed.

def remove_vowels(string):
    output = ''
    for char in string:
        if is_consonant(char):
            output += char
    return output


# Exercise 10
# Define a function named normalize_name. 
# It should accept a string and return a valid python identifier
# steps I want to take
# make lowercase, remove whitespace, establish valid identifier
def remove_special_char(string):
    return ''.join([c for c in string if c.isalnum() or c == ' '])


def normalize_name(string):
    special_char_removed = remove_special_char(string)
    return special_char_removed.lower().strip().replace(' ', '_')



# Exercise 11
# Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(nums):
    output = []
    total = 0
    for num in nums:
        total += num
        output.append(total)
    return output