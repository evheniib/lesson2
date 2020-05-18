

def take_age():
    switcher = True

    while switcher is True:
        user_str = input("Enter text")
        try:
            int(user_str)
        except ValueError:
            print("This is not a number, pls try again")
            continue
        else:
            user_age = int(user_str)
            print(f"So you are {user_age}`th years old!")
            check_age(user_age)
            switcher = False
            
    return user_age
   
def check_age(age):
    if age == 0:
        print("Thirstly you must to be born")
    elif age in range(1,7):
        print("Probably you are child in kindergarten")
    elif age in range(7, 16):
        print("You are student in school")
    else:
        print("In medival times after 16 years every human is adult")
    
my_age = take_age()
print("Task is complite my age is {age}".format(age = my_age))