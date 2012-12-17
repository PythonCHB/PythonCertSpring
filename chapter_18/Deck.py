#! /usr/bin/env python
#
# This is a simulation of a card game

import random  # we need this to shuffle a Deck object

class Card(object):
    """represents a standard playing card."""

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', 
              '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit_or_code=0, rank=2):
        """Create a card object.  There are two ways to do it: pass in encoded
values (which is what Downey does) or pass in a string of the form rank,suit
where rank is A, 1 to 10, J, Q, K and suit is S, H, D, C

The default value is the 2 of clubs """
        if type(suit_or_code) == int :
            self.suit = suit_or_code
            self.rank = rank
        elif type(suit_or_code) == str :
            self.suit, self.rank = encode(suit_or_code)
        else :
            raise TypeError('Card first argument should be an integer or a '+\
                            'decoded string')

    def encode(self, string_rep ) :
        """This method returns a tuple of encoded values for a card string.  See
the definition of the __init__ function for a description of the encoded values.
The input is a string of the form "2 of hearts", "King of Diamonds", etc."""
        import re
        card_list = string_rep.split()
        rank=card_list[0]
        suit=card_list[2]
        for s in range(len(suit_names)) :
            if suit == suit_names[s] :
                break
        else :
            raise ValueError("passed an invalid value for the suit %s of a card" %
                             suit )
        for r in range(len(rank_names)) :
            if rank == rank_names[r] :
                break
        else :
            raise ValueError("passed an invalid value for the rank of a card" %
                             rank )
        
        return s, r

    def decode(self, suit, rank ) :
        """This method converts an encoded suit and rank combination into a
string"""
        return rank_names[rank]+" of "+suit_names[suit]


    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __cmp__(self, other):
        """This is the __cmp__ method defined in Prof. Downey's book
http://www.greenteapress.com/thinkpython/html/book019.html """
        t1 = self.suit, self.rank       # Form this card into a tuple
        t2 = other.suit, other.rank     # Form the other card into a tuple, too
        return cmp(t1, t2)
    
class Deck(object):
    """The method creates a Deck object, which is a list of 52 Card objects"""
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
        self.card_idx = 0

    
    def __str__(self):
        """This produces a single string, which the __str__ method is supposed
to do, but the string has 52 lines in it"""
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def __iter__(self) :
        """Returns an iterable object.  In this case, a Deck object is iterable
    because it implements a next() function which raises StopIteration when it comes
    to the end of the Deck"""
        return self

    def next(self) :
        """Returns a list for the caller to iterate over.  Since the Deck is just a
    list of Cards, return the list"""
        if self.card_idx < len(self.cards) :
            c = self.cards[self.card_idx]
            self.card_idx += 1
            return c
        else :
            self.card_idx = 0     # for the next time we want to iterate over a Deck
            raise StopIteration




    def sort(self) :
        """This method sorts a deck.  It uses the __cmp__ method defined in
class Card """
        self.cards.sort(cmp=Card.__cmp__)
        return None

    def shuffle(self):
        """This method does an in-place shuffle of the Deck object it is called
on"""
        random.shuffle(self.cards)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def move_cards(self, hand, num):
        """Move num cards from this Deck object to Deck object hand"""
        for i in range(num):
            hand.add_card(self.pop_card())

# The problem statement for problem 18-3 says:
# Write a Deck method called deal_hands that takes two parameters, the number
# of hands and the number of cards per hand, and that creates new Hand objects,
# deals the appropriate number of cards per hand, and returns a list of Hand
# objects.
# However, there is a problem and that is Hand inherits from Deck, so this
# method must be in class Hand. 

    def deal_hand(self, cards_per_hand, num_of_hands) :
        list_of_hands=[]
        for n in range(num_of_hands) :
            h = Hand("Hand %d" % n)
            self.move_cards(h, cards_per_hand)
            list_of_hands.append(h)
        return list_of_hands

    
class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label


        
if __name__ == "__main__" :
    print "Testing the constructor and the __str__ function***********"
    deck = Deck()
    print deck

    print "Testing the iterator *************************************"
# Note that I don't have to know anything about the internals of a Deck object
# All I need to know is that a Deck object is iterable
    for card in deck:
        print card

    print "Testing shuffle================"
    deck.shuffle()
# As a nice side effect, this tests that can I run the iterator more than once
# on an object
    for card in deck:
        print card
    
    print "Testing sort+++++++++++++++++++++++++++"
    deck.sort()
    print deck

    print "Testing deal hands 5 cards/hand 4 hands -----------------------"
    list_of_hands = deck.deal_hand(5, 4 )
    for h in list_of_hands :
        print h.label
        print h
        print "----------"
    
