from copy import deepcopy
import random

VALUES = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
SUITES = ['S', 'D', 'C', 'H']

class Card():
    def __init__(self, value, suite):
        self.value = value
        self.suite = suite


CARDS = []

for val in VALUES:
    for suite in SUITES:
        CARDS.append(Card(val, suite))



NUM_PLAYERS = 6
STARTING_MONEY = 100
SB = 10
BB = 20


class Player():
    def __init__(self, money):
        self.money = money
        self.cards = []
    
    def give_card(self, card: Card):
        self.cards.append(card)

    def get_cards(self):
        return self.cards
    
    def get_money(self):
        return self.money



class Game():
    def __init__(self, num_players = NUM_PLAYERS):
        self.num_players = num_players
        self.cards = deepcopy(CARDS)
        self.community_cards = []
        self.players = []

        for _ in range(num_players):
            self.players.append(Player(STARTING_MONEY))
        
        self.dealer_pidx = 0
        self.sb_pidx = 1
        self.bb_pidx = 2
        self.curr_turn = 3

    
    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        for _ in range(2):
            for p in self.players:
                p.give_card(self.cards.pop())
    
    def rotate(self):
        self.bb_pidx = (self.bb_pidx+1) % self.num_players
        self.sb_pidx = (self.sb_pidx+1) % self.num_players
        self.dealer_pidx = (self.dealer_pidx+1) % self.num_players

    
    def visualize(self):
        print("---------- GAME STATE ----------")

        for i, p in enumerate(self.players):
            card_1, card_2 = p.get_cards()
            money = p.get_money()

            print(f"Player {i+1}: {card_1.value}:{card_1.suite} / {card_2.value}:{card_2.suite} | Avail money: {money} ")
        
        print()
        print(f"DEALER: Player {self.dealer_pidx+1}")
        print(f"SMALL BLIND: Player {self.sb_pidx+1}")
        print(f"BIG BLIND: Player {self.bb_pidx+1}")

        print("---------- ---------- ----------")


        

g = Game()
g.shuffle()
g.deal()

    



