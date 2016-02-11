#This is a library containing some functions

def useful_function(lolspeak=False):
    if lolspeak:
        print("I iz useful.")
    else:    
        print("I am useful")

def last_element(your_list):
    return your_list[-1]

print("Welcome to the library!")
useful_function()
my_list = [1,2,3,4]
print(last_element(my_list))
