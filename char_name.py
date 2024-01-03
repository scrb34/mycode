#!/usr/bin/env python3
"""Understanding dictionaries
   {key: value, key:value, ...} """

def main():
    """runtime function"""

# Which character do you want to know about? (Starlord, Mystique, Hulk)
char_name=input(Which character do you want to know about? Starlord, Mystique, Hulk)
.title()

# What statistic do you want to know about? (real name, powers, archenemy)
char_stat=input(What statistic do you want to know about? Real name, powers, archenemy?)  
.lower()

switch = {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }
print(switch) # Displays all characters
print(type(switch)) # Proves that switch is indeed a dictionary
print( switch["Starlord"] )     # displays "Starlord" 
print( switch["Mystique"] )     # displays "Mystique"
print( switch["Hulk"] )         # displays "Hulk"

# call our main function
if __name__ == "__main__":
    main()

