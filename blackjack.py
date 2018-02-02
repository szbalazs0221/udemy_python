# This is a text based BlackJack game! Have fun!!
import random

# Global variables
spades = "\u2660"
hearts = "\u2665"
diamonds = "\u2666"
clubs = "\u2660"
suits = (spades, hearts, diamonds, clubs)
ranks = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
player_chip = 0
pool = 0
# Create classes


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return str(self.suit) + str(self.rank)


class Deck:

    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle_deck(self):
        return random.shuffle(self.cards)

    def __str__(self):
        decklist = ""
        for i in self.cards:
            decklist += i.__str__() + ' '
        return str(decklist)

    def deal(self):
        return self.cards.pop()


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = False

    def add_card(self, card):
        self.cards.append(card)
        if card.rank == 'A':
            self.ace = True
        self.value += values[card.rank]

    def calc_value(self):
        if self.value < 12 and self.ace:
            self.value += 10
        return self.value

    def __str__(self):
        current_hand = ""
        for card in self.cards:
            current_hand +=card.__str__()+' '
        return f'Your hand: {current_hand}\nValue: {self.calc_value()}'

# Other methods


def create_decks(amount):
    pass


def game_step():
    pass


def place_bet(bet):
    global player_chip
    player_chip -= bet
    return bet


def initial_setup():
    print('Hello, welcome to Blackjack! Please check the rules if you are not familiar with them -> '
          'http://hu.blackjack.org/blackjack-szabalyok/ ' 
          'Please take a seat and decide how much money you want to bring in!')

    '''player_chip=input()
    print('Deck shuffled')'''


def play_blackjack():
    pass


# main function
if __name__ == "__main__":
    initial_setup()
    d = Deck()
    d.shuffle_deck()
    print(d)
    h = Hand()
    h.add_card(d.deal())
    h.add_card(d.deal())
    h.add_card(d.deal())
    print(d)
    print(h)
