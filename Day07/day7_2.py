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
        card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10}
        try:
            card_as_int = int(card)
            return card_as_int, card
        except ValueError:
            pass

        if card in card_values:
            return card_values[card], card
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
        return max(hand[:-1], key=lambda card: cls.get_card_value(card))
    
    @classmethod
    def get_highest_set_type(cls, hand):
        if cls.is_five_of_a_kind(hand):
            return "Five of a Kind"
        elif cls.is_four_of_a_kind(hand):
            return "Four of a Kind"
        elif cls.is_full_house(hand):
            return "Full House"
        elif cls.is_three_of_a_kind(hand):
            return "Three of a Kind"
        elif cls.is_two_pair(hand):
            return "Two Pair"
        elif cls.is_one_pair(hand):
            return "One Pair"
        else:
            return "High Card"
    
    original_hand = []

    @classmethod
    def get_best_hand_with_jokers(cls, hand):
        joker_count = hand.count('J')
        cls.original_hand = hand[:] 
        if joker_count > 0:
            highest_set_type = cls.get_highest_set_type(hand)

            if highest_set_type == "Five of a Kind":
                hand = cls.switch_jokerz(hand, 5)
            elif highest_set_type == "Four of a Kind":
                hand = cls.switch_jokerz(hand, 4)
            elif highest_set_type == "Full House":
            # Depends on whether there is a joker in either of the sets 
                hand = cls.switch_jokerz(hand, 3)
                hand = cls.switch_jokerz(hand, 2)
            elif highest_set_type == "Three of a Kind":
                hand = cls.switch_jokerz(hand, 3)
            elif highest_set_type == "Two Pair":
                hand = cls.switch_jokerz(hand, 2)
            elif highest_set_type == "One Pair":
                hand = cls.switch_jokerz(hand, 2)
            else:
            # Depends on highest card
                hand = cls.switch_jokerz(hand, 1)

        return hand, cls.original_hand
    
    @classmethod
    def find_repeated_element(cls, hand, count):
        for element in set(hand[:-1]):
            if hand[:-1].count(element) == count:
                return element
        return None
    
    @classmethod
    def switch_jokerz(cls, hand, count):
        high_card = cls.get_high_card(hand)
        if count == 1:
            for i in range(len(hand[:-1])):
                if hand[i] == 'J':
                    hand[i] = cls.get_high_card(hand)
            return hand
        repeated_element = cls.find_repeated_element(hand, count)
        if repeated_element is not None:
            for i in range(len(hand[:-1])):
                if hand[i] == 'J':
                    if repeated_element != 'J':
                        hand[i] = repeated_element
                    elif count != 5:
                        hand[i] = cls.get_high_card(hand)
                    else:
                        hand[i] = 'A'
        return hand

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
            print(hand_order)
            flattened_list = [hand for hands_list in hand_order.values() for hand in hands_list]
            for i, hand in enumerate(flattened_list):
                total += (count - i) * hand[5]
                print(count-i, hand[5])
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
        new_hand, old_hand = CardHand.get_best_hand_with_jokers(hand)
        # print(new_hand, old_hand)
        if CardHand.is_five_of_a_kind(new_hand):
            scores["Five"].append(old_hand)
        elif CardHand.is_four_of_a_kind(new_hand):
            scores["Four"].append(old_hand)
        elif CardHand.is_full_house(new_hand):
            scores["FH"].append(old_hand)
        elif CardHand.is_three_of_a_kind(new_hand):
            scores["Three"].append(old_hand)
        elif CardHand.is_two_pair(new_hand):
            scores["TPair"].append(old_hand)
        elif CardHand.is_one_pair(new_hand):
            scores["Pair"].append(old_hand)
        else:
            scores["HC"].append(old_hand)
        # bid_amount = CardHand.calculate_bid_amount(hand)
        # print(f"The bid amount for the hand {hand} is: {bid_amount}")
        # print(f"Five of a kind: {CardHand.is_five_of_a_kind(hand)}")
        # print(f"Four of a kind: {CardHand.is_four_of_a_kind(hand)}")
        # print(f"Full house: {CardHand.is_full_house(hand)}")
        # print(f"Three of a kind: {CardHand.is_three_of_a_kind(hand)}")
        # print(f"Two pair: {CardHand.is_two_pair(hand)}")
        # print(f"One pair: {CardHand.is_one_pair(hand)}")
        # print(f"High card: {CardHand.get_high_card(hand)}")
        # CardHand.get_best_hand_with_jokers(old_hand)

    return scores

def compute_order(classifications):
    card_order = "J123456789TQKA"
    for key, value in classifications.items():
        classifications[key] = sorted(value, key=lambda x: (card_order.index(x[0]), card_order.index(x[1]), card_order.index(x[2]), card_order.index(x[3]), card_order.index(x[4])), reverse=True)
    
    return classifications


if __name__ == "__main__":
    main()
