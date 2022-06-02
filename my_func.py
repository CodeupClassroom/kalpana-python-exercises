def is_vowel(string):
    ''' return if input item is the number two or the string two'''
    
    return string.lower() in ['a','e','i','o', 'u']

def calculate_tip(tip_percentage, total_bill):
    ''' takes in tip percentage and total bill and returns the amount of the tip'''
    
    return total_bill * (tip_percentage/100)

def get_letter_grade(number):
    ''' takes in a number returns corresponding letter grade'''
    
    if number >= 90:
        
        return 'A'
    
    elif number >= 80:
        
        return 'B'
    
    elif number >= 70:
        
        return 'C'
    
    else:
        
        return 'F'
