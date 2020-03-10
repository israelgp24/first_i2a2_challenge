from poker_hand.evaluator import evaluate_cards


class PokerHand:

    def __init__(self, hand1):
        self.hand1 = hand1
        self.score1 = evaluate_cards(*hand1.split())

    def compare_with(self, hand2):
        score2 = hand2.score1
        if self.score1 < score2:
            return 'WIN'
        elif self.score1 > score2:
            return 'LOSS'
        else:
            return 'TIE'
