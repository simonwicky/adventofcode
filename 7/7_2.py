#!/usr/bin/env python

"""
To make things a little more interesting, the Elf introduces one additional rule. Now, J cards are jokers - wildcards that can act like whatever card would make the hand the strongest type possible.

To balance this, J cards are now the weakest individual cards, weaker even than 2. The other cards stay in the same order: A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J.

J cards can pretend to be whatever card is best for the purpose of determining hand type; for example, QJJQ2 is now considered four of a kind. However, for the purpose of breaking ties between two hands of the same type, J is always treated as J, not the card it's pretending to be: JKKK2 is weaker than QQQQ2 because J is weaker than Q.

Now, the above example goes very differently:

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
32T3K is still the only one pair; it doesn't contain any jokers, so its strength doesn't increase.
KK677 is now the only two pair, making it the second-weakest hand.
T55J5, KTJJT, and QQQJA are now all four of a kind! T55J5 gets rank 3, QQQJA gets rank 4, and KTJJT gets rank 5.
With the new joker rule, the total winnings in this example are 5905.

Using the new joker rule, find the rank of every hand in your set. What are the new total winnings?
"""

import functools


#type defined as follow :
#5 of a kind is 7
#4 of a kind is 6
#full house is 5
#3 of a kind is 4
#two pairs is   3
#one pair is    2
#high card is   1
def hand_type(hand_orig):
	hand_type = 1
	for new_j in '23456789TQKA':
		hand = hand_orig.replace('J',new_j)
		hand_set_len = len(set(hand))
		if hand_set_len == 1: #5 of a kind
			return 7
		if hand_set_len == 4: #one pair
			hand_type = max(2, hand_type)
		if hand_set_len == 3: #two pair or 3 of a kind
			for c in hand[:3]:
				if hand.count(c) == 3:
					hand_type = max(4, hand_type)
			hand_type = max(3, hand_type)
		if hand_set_len == 2: #4 of a kind or full house
			for c in hand[:2]:
				if hand.count(c) == 4:
					hand_type = max(6, hand_type)
			hand_type = max(5, hand_type)
	return hand_type


def cmp_hands(hands_a_ext, hands_b_ext):
	order = 'J23456789TQKA'
	hands_a = hands_a_ext[0]
	hands_b = hands_b_ext[0]

	hand_type_cmp = hand_type(hands_a) - hand_type(hands_b)
	if hand_type_cmp != 0:
		return hand_type_cmp

	for i in range(len(hands_a)):
		if order.index(hands_a[i]) < order.index(hands_b[i]):
			return -1
		if order.index(hands_a[i]) > order.index(hands_b[i]):
			return 1
	return 0



with open('input','r') as f:
	lines = f.read().splitlines()

hands = [(line.split()[0], int(line.split()[1])) for line in lines]


hands = sorted(hands,key=functools.cmp_to_key(cmp_hands))
print(sum([(rank + 1) * value[1] for rank, value in enumerate(hands)]))





