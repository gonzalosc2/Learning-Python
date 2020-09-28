####################################
# author: Gonzalo Salazar
# course: 2020 Complete Python Bootcamps: From Zero to Hero in Python
# purpose: creating a game as a warm up exercise (card game: War)
# description: main file
####################################

#cd ..
#cd Python/Udemy_PythonBootcamp/WarmUpEx_War
from classes_war import *

### Game setup ###
player_one = Player('One')
player_two = Player('Two')

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.draw_card())
    player_two.add_cards(new_deck.draw_card())

#checking
#len(player_one.all_cards)
#print(player_one.all_cards[0])

### Game - while ###
game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(f'Round {round_num}')

    if len(player_one.all_cards) == 0:
        print('Player One is out of cards! Player Two wins!')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print('Player Two is out of cards! Player One wins!')
        game_on = False
        break

    # NEW ROUND
    player_one_cards = []  # player one's cards in hand
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    # CONDITON CHECKING
    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False

        else:
            print('WAR!')

            if len(player_one.all_cards) < 5:
                print('Player One unable to declare war')
                print('PLAYER TWO WINS!')
                game_on = False
                break

            if len(player_two.all_cards) < 5:
                print('Player Two unable to declare war')
                print('PLAYER ONE WINS!')
                game_on = False
                break

            for num in range(5):
                player_one_cards.append(player_one.remove_one())
                player_two_cards.append(player_two.remove_one())
