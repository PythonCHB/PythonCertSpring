#!/usr/bin/env python

"""
application logic code for ultra simple 
address book app...
"""

import json

class AddressBook(object):
    """
    very simple data model -- just a list of dicts
    """
    def __init__(self):
        self.book = []
        self.filename = "a_book.json"

    def save_to_file(self, filename=None):
	if filename != None :
            self.filename = filename
        json.dump(self.book, open(filename, 'wb'), indent=4 )

    def load_from_file(self, filename=None):
	if filename != None :
            self.filename = filename
        self.book = json.load( open(filename, 'rb') )


if __name__ == "__main__":
    import pprint
    a_book = AddressBook()
    a_book.load_from_file()

    pprint.pprint(a_book.book)

