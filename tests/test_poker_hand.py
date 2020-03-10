import unittest
import json
import os

from poker_hand.evaluator import evaluate_cards
from poker_hand.poker_hand import PokerHand


class TestEvaluator(unittest.TestCase):

    def test_5cards_new(self):
        poker_hand_1 = PokerHand("TS TH TD JH JD")
        poker_hand_2 = PokerHand("JH JD TH TC 4C")
        result = poker_hand_1.compare_with(poker_hand_2)
        self.assertTrue(PokerHand("TC TH 5C 5H KH").compare_with(
            PokerHand("9C 9H 5C 5H AC")) == 'WIN')
        self.assertTrue(PokerHand("TS TD KC JC 7C").compare_with(
            PokerHand("JS JC AS KC TD")) == 'LOSS')
        self.assertTrue(PokerHand("7H 7C QC JS TS").compare_with(
            PokerHand("7D 7C JS TS 6D")) == 'WIN')
        self.assertTrue(PokerHand("5S 5D 8C 7S 6H").compare_with(
            PokerHand("7D 7S 5S 5D JS")) == 'LOSS')
        self.assertTrue(PokerHand("AS AD KD 7C 3D").compare_with(
            PokerHand("AD AH KD 7C 4S")) == 'LOSS')
        self.assertTrue(PokerHand("TS JS QS KS AS").compare_with(
            PokerHand("AC AH AS AS KS")) == 'WIN')
        self.assertTrue(PokerHand("TS JS QS KS AS").compare_with(
            PokerHand("TC JS QC KS AC")) == 'WIN')
        self.assertTrue(PokerHand("TS JS QS KS AS").compare_with(
            PokerHand("QH QS QC AS 8H")) == 'WIN')
        self.assertTrue(PokerHand("AC AH AS AS KS").compare_with(
            PokerHand("TC JS QC KS AC")) == 'WIN')
        self.assertTrue(PokerHand("AC AH AS AS KS").compare_with(
            PokerHand("QH QS QC AS 8H")) == 'WIN')
        self.assertTrue(PokerHand("TC JS QC KS AC").compare_with(
            PokerHand("QH QS QC AS 8H")) == 'WIN')
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(
            PokerHand("JH JC JS JD TH")) == 'WIN')
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(
            PokerHand("4H 5H 9H TH JH")) == 'WIN')
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(
            PokerHand("7C 8S 9H TH JH")) == 'WIN')
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(
            PokerHand("TS TH TD JH JD")) == 'WIN')
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(
            PokerHand("JH JD TH TC 4C")) == 'WIN')
        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(
            PokerHand("4H 5H 9H TH JH")) == 'WIN')
        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(
            PokerHand("7C 8S 9H TH JH")) == 'WIN')
        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(
            PokerHand("TS TH TD JH JD")) == 'WIN')
        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(
            PokerHand("JH JD TH TC 4C")) == 'WIN')
        self.assertTrue(PokerHand("4H 5H 9H TH JH").compare_with(
            PokerHand("7C 8S 9H TH JH")) == 'WIN')
        self.assertTrue(PokerHand("4H 5H 9H TH JH").compare_with(
            PokerHand("TS TH TD JH JD")) == 'LOSS')
        self.assertTrue(PokerHand("4H 5H 9H TH JH").compare_with(
            PokerHand("JH JD TH TC 4C")) == 'WIN')
        self.assertTrue(PokerHand("7C 8S 9H TH JH").compare_with(
            PokerHand("TS TH TD JH JD")) == 'LOSS')
        self.assertTrue(PokerHand("7C 8S 9H TH JH").compare_with(
            PokerHand("JH JD TH TC 4C")) == 'WIN')
        self.assertTrue(PokerHand("TS TH TD JH JD").compare_with(
            PokerHand("JH JD TH TC 4C")) == 'WIN')
