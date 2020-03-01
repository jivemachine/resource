# Ryans answers

filename = "4.6_import_exercises.py"

#how to unpack a tuple
a,b = (1,2)
a,b,c = (1,2,3)


with open(filename, "r") as f:
    contents = f.readlines()
    for i, line in enumerate(contents, start = 1):
        print(i, line)



def make_grocery_list(grocery_list):
    filename = "my_grocery_list.txt"
    with open(filename, "a") as f:
        for item in grocery_list:
            f.write(item + "\n")


def show_grocery_list():
    with open("my_grocery_list.txt") as f:
        contents = f.readlines()
        for item in contents:
            print(item)

show_grocery_list()  

def buy_item(item, grocery_list):
    grocery_list.remove(item)
    print(grocery_list)
