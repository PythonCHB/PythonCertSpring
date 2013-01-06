#! /usr/bin/env python
#
# Write a Deck method named sort that uses the list method sort to sort the
# cards in a Deck. sort uses the __cmp__ method we defined to determine sort
# order.


import Deck

def main() :
    deck = Deck.Deck()
    deck.shuffle()
    print "*************** After shuffling the deck:"
    print deck
    deck.sort()
    print "************** After sorting the deck:"
    print deck
    
if __name__ == "__main__" :
    main()
    
