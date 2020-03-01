


def is_two(x):
    if (x == 2) or (x == "two"):
        return True
    else:
        return False 



def is_vowel(x):
    vowels = "aeiouAEIOU"
    if x in vowels:
        return True
    else:
        return False    


def is_consonant(x):
    vowels = "aeiouAEIOU"
    if x in vowels:
        return False
    else:
        return True




def capitalize_me(x):
    vowels = "aeiouAEIOU"
    if x[0] not in vowels:
        return x.capitalize()
    else:
        return x



def calculate_tip(total, percentage):
    if percentage == 0:
        return 0
    elif percentage == 1:
        return total * 0.01
    else:
        return 0



def apply_discount(price, discount):
    return price - (discount * 0.1)



def handle_commas(string):
    newstring = string.replace("," , "")
    return newstring


def get_letter_grade(x):
    if x >= 90:
        return "A"
    elif x >= 80:
        return "B"
    elif x >= 70:
        return "C"
    else:
        return "F"




def remove_vowels(string):
    vowels = "aeiouAEIOU"
    for letter in string:
        if letter in vowels:
            string = string.replace(letter , "")
    return string



def normalize_name(string):
    string = string.strip()
    string = string.lower()
    string = string.replace(" ", "_")
    return string



def cumsum(number):
    result = []
    total = 0
    for num in number:
        total += num
        result.append(total)
    return result



def twelveto24(time_string):
    if time_string[-2:] == "AM" and time_string[:2] == "12":
        return "00" + time_string[2:-2]
    elif time_string[-2:] == "AM":
        return time_string[:-2]
    elif time_string[-2:] == "PM" and time_string[:2] == "12":
        return time_string[:-2]
    else:
        return str(int(time_string[:2]) + 12) + time_string[2:8]
        
            
