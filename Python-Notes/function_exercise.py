# 1 Define a function named is_two.
#  It should accept one input and return True if the passed input is either the number or the string 2, 
# False otherwise.

def is_two(x):
    if (x == 2) or (x == "two"):
        return True
    else:
        return False 


# 2 Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(x):
    vowels = "aeiouAEIOU"
    if x in vowels:
        return True
    else:
        return False

# 3 Define a function named is_consonant. 
# It should return True if the passed string is a consonant, False otherwise. 
# Use your is_vowel function to accomplish this.
def is_consonant(x):
    vowels = "aeiouAEIOU"
    if x in vowels:
        return False
    else:
        return True

# 4 Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word if the word starts with a consonant.
def capitalize_me(x):
    vowels = "aeiouAEIOU"
    if x[0] not in vowels:
        return x.capitalize()
    else:
        return x

# 5 Define a function named calculate_tip.
#  It should accept a tip percentage (a number between 0 and 1) 
# and the bill total, and return the amount to tip.

def calculate_tip(total, percentage):
    if percentage == 0:
        return 0
    elif percentage == 1:
        return total * 0.01
    else:
        return 0


# 6 Define a function named apply_discount. 
# It should accept a original price, and a discount percentage, 
# and return the price after the discount is applied.

def apply_discount(price, discount):
    return price - (discount * 0.1)

# 7 Define a function named handle_commas. 
# It should accept a string that is a number that contains commas in it as input, 
# and return a number as output.

def handle_commas(string):
    newstring = string.replace("," , "")
    return newstring

# 8 Define a function named get_letter_grade. 
# It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(x):
    if x >= 90:
        return "A"
    elif x >= 80:
        return "B"
    elif x >= 70:
        return "C"
    else:
        return "F"

# 9 Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(string):
    vowels = "aeiouAEIOU"
    for letter in string:
        if letter in vowels:
            string = string.replace(letter , "")
    return string

# 10 Define a function named normalize_name. 
# It should accept a string and return a valid python identifier, that is:
#--anything that is not a valid python identifier should be removed
#--leading and trailing whitespace should be removed
#--everything should be lowercase
#--spaces should be replaced with underscores
#--for example:
Name will become name
First Name will become first_name
% Completed will become completed



def normalize_name(string):
    string = string.strip()
    string = string.lower()
    string = string.replace(" ", "_")
    return string


# 11 Write a function named cumsum that accepts 
# a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
cumsum([1, 1, 1]) returns [1, 2, 3]
cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumsum(num):
    for n in num:
        total = 0
        sums = []
        newtotal = total + n
        sums.append(newtotal)
    return sums


    def cumsum(nums):
        cumlist = []
        length = len(nums)
        cumlist = [sum(nums[0 + 1]) for x in range(0, length)
        return cumlist

numbers = [4,3,6]

sums = []

def cumsum(numbers):
    sums.append(numbers[0])
    for i in range(len(numbers) - 1):
        if i == 0:
            sums.append(numbers[i] + numbers[i + 1])
        else:
            sums.append(numbers[i + 1] + sums[i])
    return sums


def cumsum(num):
    for n in range(len(num) - 1):



number = [1,2,3]
result = []
total = 0

#This is the answer -----------
def cumsum(number):
    result = []
    total = 0
    for num in number:
        total += num
        result.append(total)
    return result

# BONUS:

# 1 Create a function named twelveto24.
#  It should accept a string in the format 10:45am or 4:30pm and return a string 
# that is the representation of the time in a 24-hour format. 
# Bonus write a function that does the opposite.

def twelveto24(time_string):
    if time_string[-2:] == "AM" and time_string[:2] == "12":
        return "00" + time_string[2:-2]
    elif time_string[-2:] == "AM":
        return time_string[:-2]
    elif time_string[-2:] == "PM" and time_string[:2] == "12":
        return time_string[:-2]
    else:
        return str(int(time_string[:2]) + 12) + time_string[2:8]


def twentyfourto12(time_string):
    if time_string[-2:] == "AM" and time_string[:2] == "12"




# 2 Create a function named col_index. 
# It should accept a spreadsheet column name, and return the index number of the column.
col_index('A') returns 1
col_index('B') returns 2
col_index('AA') returns 27

def col_index(column):
    for column in range(1:28):
        for letter in letter for column:
            if letter = a 


def col_index(letters):
    numbers = []
    for letter in letters:
        number = ord(letter) - 96
        number = number.lower()
        numbers.append(number)
    return numbers


print [ord(char) - 96 for char in raw_input('Write Text: ').lower()]



def col_index(text):
    total  = 0
    nums = [str(ord(x) - 96) for x in text.lower() if x >= 'a' and x <= 'z']
    newnums = int(nums)
    for n in newnums:
        total  = sum(newnums)
    return total

def alphabet_position(text):
    dictt = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8',
    'i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17',
    'r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'
    }
    arr = []
    new_text = text.lower()
    for i in list(new_text):
        for k, j in dictt.iteritems():
            if k == i:
                arr.append(j)
    return ' '.join(arr)


def col_index(text):
    x = int(text)
        if x>=1 and x<=26:
            print('letter', x, 'in the alphabet:', chr(ord('A')+(x-1)))
        else:
            print('invalid input:', x)





def col_index(text):
    total = sum([26**i * list(reversed)])