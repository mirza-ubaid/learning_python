alien_color = ['Green', 'Red', 'Yellow']
for color in alien_color:
    if color.lower() == 'green':
        print(color+" Alien, You earned %d Points!" % 5)
    elif color.lower() == 'yellow':
        print(color+" Alien, You earned %d Points!" % 10)
    elif color.lower() == 'red':
        print(color+" Alien, You earned %d Points!" % 15)
