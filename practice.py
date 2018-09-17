#!/usr/bin/env python3

def main():
    game = ['Ludo', 'Snakes and Ladders', 'Card', 'I Call On']
    print_list(game)

def print_list(x_game):
    for i in x_game: print(i, end = ' ', flush=True)

if __name__ == '__main__': main()