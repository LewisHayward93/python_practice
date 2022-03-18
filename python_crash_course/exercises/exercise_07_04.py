# Extended the problem in the book to make use of some other features
# User asked for toppings to be added, unavailable toppings have been listed and checked against with relevant reponse
# Once finished, program reads back all of the toppings selected and asks the user if this is correct before finalising response.

toppings = []

print("Please type out the toppings you'd like adding to the pizza.")
print("If the topping is not available, I will let you know!")
print("Once you're done, type 'done':")

prompt = "Topping: "
topping_request = ""

unavailable_toppings = ['ham', 'beef', 'chillies']

while topping_request != 'done':
    topping_request = input(prompt)
    if topping_request != 'done':
        if topping_request in unavailable_toppings:
            print("I'm sorry this isn't available, please choose another:")
        else:
            print(f"{topping_request.title()} has been added to your pizza!")
            toppings.append(topping_request)

print("You have chosen a pizza with the following toppings: ")
for topping in toppings:
    print(f"\t {topping.title()}")


validate_order = input("Is this correct? Type 'y' for yes and 'n' for no: ")

if validate_order == 'n':
    print("Should have paid attention then...")
else:
    print("Your order is on the way!")
