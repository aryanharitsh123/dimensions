#Copyright (c) 2009, Walter Bender

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

import pygtk
pygtk.require('2.0')
import gtk
import gobject
import random

from sprites import *
from constants import *
from card import *

#
# class for defining deck of cards
#
class Deck:
    def __init__(self, vmw):
        # create the deck of cards
        self.deck = {}
        # remember the position in the deck
        self.index = 0
        # how many cards are in the deck?
        self.count = 0
        # Initialize the deck of cards by looping through all the patterns
        for shape in range(0,SHAPES):
            for color in range(0,COLORS):
                for num in range(0,NUMBER):
                    for fill in range(0,FILLS):
                        self.deck[self.count] = Card(vmw,shape,color,num,fill)
                        self.count += 1

    # shuffle the deck
    def shuffle(self):
        # hide all the cards
        for c in self.deck:
            self.deck[c].hide_card()
        # randomize the deck
        for n in range(0,DECKSIZE*4):
            i = random.randrange(DECKSIZE)
            j = random.randrange(DECKSIZE)
            self.swap_cards(i,j)            
        # reset the index to the beginning of the deck after a shuffle
        self.index = 0
        return

    # swap the position of two cards in the deck
    def swap_cards(self,i,j):
        tmp = self.deck[j]
        self.deck[j] = self.deck[i]
        self.deck[i] = tmp
        return

    # given a sprite, find the corresponding card in the deck
    def spr_to_card(self, spr):
        for c in self.deck:
            if self.deck[c].spr == spr:
                return self.deck[c]
        return None

    # deal the next card from the deck
    def deal_next_card(self):
        self.index += 1
        if self.empty():
            return None
        return self.deck[self.index]
 
    # is the deck empty?
    def empty(self):
        if self.index < self.count:
            return False
        else:
            return True

    # hide the deck
    def hide(self):
        for c in self.deck:
            self.deck[c].hide_card()
