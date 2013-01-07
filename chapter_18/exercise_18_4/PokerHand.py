# -*- coding: utf-8 -*-
"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

# Exercise 5  
# The following are the possible hands in poker, in increasing order of value
#(and decreasing order of probability):
# pair:  two cards with the same rank
# two pair: two pairs of cards with the same rank
# three of a kind: three cards with the same rank
# straight: five cards with ranks in sequence (aces can be high or low, so
# Ace-2-3-4-5 is a straight and so is 10-Jack-Queen-King-Ace, but
# Queen-King-Ace-2-3 is not.)
# flush: five cards with the same suit
# full house: three cards with one rank, two cards with another
# four of a kind: four cards with the same rank
# straight flush: five cards in sequence (as defined above) and with the same
# suit
# The goal of these exercises is to estimate the probability of drawing these
# various hands.
# Download the following files from thinkpython.com/code:
# Card.py: A complete version of the Card, Deck and Hand classes in this
# chapter.
# PokerHand.py: An incomplete implementation of a class that represents a poker hand, and some code that tests it.
# If you run PokerHand.py, it deals seven 7-card poker hands and checks to see if any of them contains a flush.
# Read this code carefully before you go on.
# Add methods to PokerHand.py named has_pair, has_twopair, etc. that return True or False according to whether or not the hand meets the relevant criteria. Your code should work correctly for “hands” that contain any number of cards (although 5 and 7 are the most common sizes).
# Write a method named classify that figures out the highest-value classification for a hand and sets the label attribute accordingly. For example, a 7-card hand might contain a flush and a pair; it should be labeled “flush”.
# When you are convinced that your classification methods are working, the next step is to estimate the probabilities of the various hands. Write a function in PokerHand.py that shuffles a deck of cards, divides it into hands, classifies the hands, and counts the number of times various classifications appear.
# Print a table of the classifications and their probabilities. Run your
# program with larger and larger numbers of hands until the output values
# converge to a reasonable degree of accuracy. Compare your results to the
# values at wikipedia.org/wiki/Hand_rankings

from Card import *


class PokerHand(Hand):

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self) :
        """Builds a histogram of the ranks that appear in the hand.

        Stores the result in attribute ranks.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_pair(self):
        """pair:  two cards with the same rank"""

        for val in self.ranks.values() :
            if val >= 2 :
                return True
        return False

    def has_two_pairs(self) :
        """ two pair: two pairs of cards with the same rank"""
        pair_ctr=0
        for val in self.ranks.values() :
            if val >= 2 :
                pair_ctr += 1
                if pair_ctr >= 2 :
                    return True
        return False

    def has_three_of_a_kind(self) :
        """three of a kind: three cards with the same rank"""
        for val in self.ranks.values() :
            if val >= 3 :
                return True
        return False

    

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        for val in self.suits.values():
            if val >= 5:
                return True
        return False


if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    while True:
        print "*"*20
        try :
            hand = PokerHand()
        except IndexError:
            print "New Deck"
            deck = Deck()
            deck.shuffle()
        deck.move_cards(hand, 7)
        hand.sort()
        hand.suit_hist()
        hand.rank_hist()
        print hand
        print "Has flush:",  hand.has_flush()
        print "Has pair:", hand.has_pair()
        print "Has two pairs:", hand.has_two_pairs()
        t = hand.has_three_of_a_kind()
        print "Has three of a kind:", t
        if t:
            break

    
        
        

