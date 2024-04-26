# must 1st understand scope to understand closures

# Closure is a function having access to the scope of its parent function
# after the parent function has returned 
# nested function 

print("---------- nested function ------------")
# parent function 
def parent_function():
    print("Hello, ")
    # nested function, has access to scope of parent function 
    def nested_function():
        print("Wolrd!")

    nested_function()

parent_function()

print()
print("---------- Closures nested function ------------")
# parent function 
def parent_function(person):
    # Scope of parent function
    coins = 3
    # nested function, has access to scope of parent function 
    def play_game():
        # must use nonlocal, because changing value of 'coins'
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.\n")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.\n")
        else:
            print("\n" + person + " out of coins.\n")
    
    # CLOSURE WHEN RETURN keeping different values in coins inside scope of parent function 
    # that play_game function can access value of even when change value of 

    # returning nested function not calling into action 
    return play_game


empress = parent_function("Empress")
jenny = parent_function("Jenny")

# returning empress as a function 
empress()
empress()

jenny()



print()
print("---------- Closures nested function ------------")
# parent function 
def parent_function(person, coins):
    # Scope of parent function
    
    # nested function, has access to scope of parent function 
    def play_game():
        # must use nonlocal, because changing value of 'coins'
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.\n")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.\n")
        else:
            print("\n" + person + " out of coins.\n")
    
    # CLOSURE WHEN RETURN keeping different values in coins inside scope of parent function 
    # that play_game function can access value of even when change value of 

    # returning nested function not calling into action 
    return play_game


empress = parent_function("Empress", 3)
jenny = parent_function("Jenny", 5)

# returning empress as a function 
empress()
empress()
empress()

jenny()
jenny()
jenny()