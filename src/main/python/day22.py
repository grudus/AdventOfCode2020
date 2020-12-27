from functools import reduce
from collections import defaultdict

def first_star(player1_deck, player2_deck):
    while player1_deck and player2_deck:
        player1_card = player1_deck[0]
        player2_card = player2_deck[0]
        player1_deck = player1_deck[1:]
        player2_deck = player2_deck[1:]

        if player1_card > player2_card: player1_deck += [player1_card, player2_card]
        else: player2_deck += [player2_card, player1_card]

    return calculate_points(player1_deck if player1_deck else player2_deck)


def second_star(player1_deck, player2_deck):
    (_, winner_deck) = play_recursively(player1_deck, player2_deck, set())
    return calculate_points(winner_deck)


def play_recursively(player1_deck, player2_deck, memory):
    while player1_deck and player2_deck:
        decks_id = (tuple(player1_deck), tuple(player2_deck))
        if decks_id in memory: return (1, player1_deck)
        memory.add(decks_id)
        
        player1_card = player1_deck[0]
        player2_card = player2_deck[0]
        player1_deck = player1_deck[1:]
        player2_deck = player2_deck[1:]
    
        if len(player1_deck) >= player1_card and len(player2_deck) >= player2_card:
            (winner_id, _) = play_recursively(player1_deck[:player1_card], player2_deck[:player2_card], set())

            if winner_id == 1: player1_deck += [player1_card, player2_card]
            else: player2_deck += [player2_card, player1_card]

        elif player1_card > player2_card: player1_deck += [player1_card, player2_card]
        else: player2_deck += [player2_card, player1_card]

    return (1, player1_deck) if player1_deck else (2, player2_deck)


def calculate_points(winner): return reduce(int.__add__, [card * (index + 1) for index, card in enumerate(reversed(winner))])


if __name__ == "__main__":
    player1_deck, player2_deck = open('src/main/resources/day22/input.txt', 'r').read().split("\n\n")
    player1_deck, player2_deck = [int(card) for card in player1_deck.split("\n")[1:]], [int(card) for card in player2_deck.split("\n")[1:]]
    print(first_star(player1_deck[:], player2_deck[:]))
    print(second_star(player1_deck, player2_deck))