# the input() function allows the programmer to take in input from the user

name = input("What is your name?\n")
print(f"Hello {name}")

# using multiline prompts

prompt = "This is a multiline prompt..."
prompt += "\nWhat is your name?\n"

name = input(prompt)
print(f"Hello {name}")

# input() function use means everything take from user is string. Convert to int for any calculations

response = input("How old are you?\n")
age = int(response)

if age >= 18:
    print("You are of legal age.")
else:
    print("You are not of legal age.")

prompt = "Tell me something about you and i'll repeat it back\n"
prompt += "Type 'quit' to escape\n"

message = ""

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
