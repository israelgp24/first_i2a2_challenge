from poker_hand.evaluator_hand import evaluate_5cards

rank_map = {
    '2': 0,
    '3': 1,
    '4': 2,
    '5': 3,
    '6': 4,
    '7': 5,
    '8': 6,
    '9': 7,
    'T': 8,
    'J': 9,
    'Q': 10,
    'K': 11,
    'A': 12
}

suit_map = {
    'C': 0,
    'D': 1,
    'H': 2,
    'S': 3,
    'c': 0,
    'd': 1,
    'h': 2,
    's': 3
}


def evaluate_cards(*args):
    if isinstance(args[0], str):
        cards = []
        for arg in args:
            cards.append(rank_map[arg[0]] * 4 + suit_map[arg[1]])
    else:
        cards = tuple(args)

    if len(args) == 5:
        return evaluate_5cards(*cards)
