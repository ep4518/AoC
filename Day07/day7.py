#!/usr/bin/env python3
import sys

class CardHand:
    def __init__(self, hand):
        self.hand = hand

    @classmethod
    def calculate_bid_amount(cls, hand):
        return hand[-1]

    @staticmethod
    def get_card_value(card):
        card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
        try:
            card_as_int = int(card)
            return card_as_int
        except ValueError:
            pass

        if card in card_values:
            return card_values[card]
        else:
            print(f"Card: {card}")
            raise ValueError(f"Invalid card: {card}")

    
    @classmethod
    def is_five_of_a_kind(cls, hand):
        return any(hand.count(card) == 5 for card in set(hand[:-1]))
    
    @classmethod
    def is_four_of_a_kind(cls, hand):
        return any(hand.count(card) == 4 for card in set(hand[:-1]))

    @classmethod
    def is_full_house(cls, hand):
        return cls.is_three_of_a_kind(hand) and cls.is_one_pair(hand)

    @classmethod
    def is_three_of_a_kind(cls, hand):
        return any(hand.count(card) == 3 for card in set(hand[:-1]))

    @classmethod
    def is_two_pair(cls, hand):
        pairs = [card for card in set(hand[:-1]) if hand.count(card) == 2]
        return len(pairs) == 2

    @classmethod
    def is_one_pair(cls, hand):
        return any(hand.count(card) == 2 for card in set(hand[:-1]))

    @classmethod
    def get_high_card(cls, hand):
        print(f"Hand: {hand}")
        return max(cls.get_card_value(card) for card in hand[:-1])

def main():
    total = 0
    if len(sys.argv) != 2:
        print("Improper Usage: python day5.py [.txt]")
        sys.exit(1)
    
    try:
        with open(sys.argv[1], 'r') as file:
            rows = file.readlines()
            rows, count = parse(rows)
            hand_classification = compute_classification(rows)
            hand_order = compute_order(hand_classification)
            flattened_list = [hand for hands_list in hand_order.values() for hand in hands_list]
            for i, hand in enumerate(flattened_list):
                total += (count - i) * hand[5]
            print(total)
    
    except FileNotFoundError:
        print(f"File '{sys.argv[1]}' not found.")
    except PermissionError:
        print(f"Permission denied for '{sys.argv[1]}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return 0
    
def parse(rows):
    new = []
    count = 0
    for i, row in enumerate(rows):
        count += 1
        row = row.split()
        characters = list(row[0])
        characters.append(int(row[1]))
        new.append(characters)

    return new, count

def compute_classification(rows):
    scores = {"Five": [], "Four": [], "FH": [], "Three": [], "TPair": [], "Pair": [], "HC": []}
    for hand in rows:
        if CardHand.is_five_of_a_kind(hand):
            scores["Five"].append(hand)
        elif CardHand.is_four_of_a_kind(hand):
            scores["Four"].append(hand)
        elif CardHand.is_full_house(hand):
            scores["FH"].append(hand)
        elif CardHand.is_three_of_a_kind(hand):
            scores["Three"].append(hand)
        elif CardHand.is_two_pair(hand):
            scores["TPair"].append(hand)
        elif CardHand.is_one_pair(hand):
            scores["Pair"].append(hand)
        else:
            scores["HC"].append(hand)
        # bid_amount = CardHand.calculate_bid_amount(hand)
        # print(f"The bid amount for the hand {hand} is: {bid_amount}")
        # print(f"Five of a kind: {CardHand.is_five_of_a_kind(hand)}")
        # print(f"Four of a kind: {CardHand.is_four_of_a_kind(hand)}")
        # print(f"Full house: {CardHand.is_full_house(hand)}")
        # print(f"Three of a kind: {CardHand.is_three_of_a_kind(hand)}")
        # print(f"Two pair: {CardHand.is_two_pair(hand)}")
        # print(f"One pair: {CardHand.is_one_pair(hand)}")
        # print(f"High card: {CardHand.get_high_card(hand)}")
    
    return scores

def compute_order(classifications):
    card_order = "123456789TJQKA"
    for key, value in classifications.items():
        classifications[key] = sorted(value, key=lambda x: (card_order.index(x[0]), card_order.index(x[1]), card_order.index(x[2]), card_order.index(x[3]), card_order.index(x[4])), reverse=True)
    
    return classifications

def face_card_value(card):
    face_cards = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return face_cards.get(card, int(card))




if __name__ == "__main__":
    main()
