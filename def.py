import random

def print_params ():
    coordinats = [12, 27, 53, 184, 305]
    place1 = random.choice(coordinats)
    coordinats.remove(place1)
    place2 = random.choice(coordinats)
    print('_first','_second')

    return place1, place2
place1, place2 =print_params()
print(place1, place2)