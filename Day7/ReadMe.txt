The answer to part 2 is 254412181.

TODO:
Fix the randomness in the generation of the score for day7_2.py.

Potential Issues:

Joker Handling: The get_best_hand_with_jokers method in the CardHand class modifies the input hand by replacing jokers with specific cards based on the hand's classification. This modification is done in place, and it seems to depend on the highest set type. This can introduce variability in the hands, affecting the final order and score.

Ordering of Hands: The compute_order function sorts the hands based on a custom order defined by the card_order string. If two hands have the same classification, their order is determined by this custom order. This could lead to variations in the final score.

Handling of Ties: In the sorting process, if two hands have the same classification and the same cards, their order is determined by their bid amounts. If bid amounts are equal, their order is preserved from the input. Depending on the input order, this could lead to different scores.

Print Statements: The code includes some print statements for debugging purposes. If these statements print information related to hands or intermediate steps, they might contribute to different outputs.
