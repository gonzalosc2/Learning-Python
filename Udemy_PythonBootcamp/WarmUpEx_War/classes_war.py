####################################
# author: Gonzalo Salazar
# course: 2020 Complete Python Bootcamps: From Zero to Hero in Python
# purpose: creating a game as a warm up exercise (card game: War)
# description: definition of classes
####################################

### Loading packages ###
import random

### Global variables ###
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',\
         'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, \
              'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, \
              'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

### Card class ###
class Card():

    def __init__(self,suit,rank):
        self.suit = suit.capitalize()
        self.rank = rank.capitalize()
        self.value = values[self.rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

#checking
#two_hearts = Card('hearts','two')
#three_of_clubs = Card('clubs','three')
#two_hearts.value < three_of_clubs.value

### Deck class ###
class Deck():

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create the card object
                created_card = Card(suit,rank)

                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def draw_card(self):
        return self.all_cards.pop()

#checking
#new_deck = Deck()
#new_deck.shuffle()
#for card_object in new_deck.all_cards:
#    print(card_object)
#my_card=new_deck.draw_card()
#len(new_deck.all_cards)

### Player class ###
class Player():

    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)  #removes the card from the top of the deck

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            # for lists of multiple card objects
            self.all_cards.extend(new_cards)
        else:
            #for a single card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

#.append(LIST/VALUE) adds a LIST/VALUE to an existing list. This causes nested
#                    lists if we use a LIST as an input.
#.extend(LIST2) merges LIST2 with the existing list.

#checking
#new_player = Player('Gonzalo')
#print(new_player)
#new_player.add_cards(my_card)
#print(new_player)
#print(new_player.all_cards[0])
