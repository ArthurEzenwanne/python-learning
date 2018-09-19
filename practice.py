#!/usr/bin/env python3

def main():
    game = ['Ludo', 'Snakes and Ladders', 'Card', 'I Call On', 'Monopoly']
    animal_sounds = {'kitten':'meows', 'puppy':'ruff!', 'lion':'roars'}
    print_list(game)
    print_animal_sounds(animal_sounds)
    
def print_list(x_game):
    for i in x_game: print(i, end = ' ', flush=True)
    
def print_animal_sounds(sounds):
    for k,v in sounds.items():
        print(f' {k} : {v}')

if __name__ == '__main__': main()