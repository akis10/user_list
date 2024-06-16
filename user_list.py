def product_list(list = []):
    """A function that asks user for products and displays them
    """
    # list = []
    products_number = input("Give a number of products ")

    # if int(products_number):
    #     for i in range(int(products_number)):
    #         user = input(f"Give me {products_number} products\n")
    #         list.append(user)
    # else:
    #     print("Invalid number of products!")
    #     product_list()
        
        
    # Try-except works better as it chatches the ValueError exception
    
    try:
        int(products_number)
        for i in range(int(products_number)):
            user = input(f"Give me {products_number} products\n")
            list.append(user)
    except ValueError:
        print("Invalid number of products!")
        
    
    try:
        int(products_number)
        print(f"Your products are {', '.join(list)}")
    except ValueError:
        print("Try again")


# Function for entering
def enter_program():
    enter = input("If you want to add items to the list, press X: ")
    if 'X' in enter or 'x' in enter:
        product_list()
    else:
        print("Wrong!")
        enter_program()
        
        
# Function for exiting
# def exit_program():
#     exit = input("If you want to exit press E")
#     if exit is 'e' or exit is 'E':
#         return 
    


enter_program()