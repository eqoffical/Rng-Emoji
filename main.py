import emoji
import random

print("Random Emoji Generator")

cldr_names = list(emoji.EMOJI_DATA.keys()) 

continue_program = True

name = random.choice(cldr_names)
print(f"\n{emoji.emojize(name)}\n")

while continue_program:

    user_input = input("Generate another random emoji? (Y/N) ")
  
    if user_input.lower() == "y":
        continue_program = True 
        name = random.choice(cldr_names)
        print(f"\n{emoji.emojize(name)}\n")
  
    elif user_input.lower() == "n":
        continue_program = False
        print("Okay, goodbye! 👋")
        
    else:
        continue_program = True
        print("Y for yes and N for no 😒👎\n")
