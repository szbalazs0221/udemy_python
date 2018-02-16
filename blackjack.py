# This is a text based BlackJack game! Have fun!!

# still left:
# define deck rearrange
# add exceptions


import random
import time
import os

# Global variables
spades = "\u2660"
hearts = "\u2665"
diamonds = "\u2666"
clubs = "\u2660"
suits = (spades, hearts, diamonds, clubs)
ranks = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

dealer = None
player = None
deck = None

player_chip = 100
pool = 0
end = False


# Classes
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
        deck_list = ""
        for i in self.cards:
            deck_list += i.__str__() + ' '
        return str(deck_list)

    def deal(self):
        return self.cards.pop(0)


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = False
        self.hidden = True

    def add_card(self, card):
        self.cards.append(card)
        if card.rank == 'A':
            self.ace = True
        self.value += values[card.rank]

    def calc_value(self):
        if self.value < 12 and self.ace:
            self.value += 10
        return int(self.value)

    def show(self):
        self.hidden = False

    def __str__(self):
        current_hand = ""
        if not self.hidden:
            for card in self.cards:
                current_hand += card.__str__()+' '
            return f'Hand:\n{current_hand}\nValue: {self.calc_value()}'
        # Need to handle if Ace value turns to 10, hidden showing calculates with 1
        elif self.ace:
            current_hand = self.cards[0].__str__() + ' ??'
            return f'Hand:\n{current_hand}\nValue: ~{self.calc_value()-11}'
        else:
            current_hand = self.cards[0].__str__() + ' ??'
            return f'Hand:\n{current_hand}\nValue: ~{self.calc_value()-values[self.cards[1].rank]}'


# Other methods
def clear():
    os.system('cls')


def welcome():
    clear()
    print('Hello, welcome to Blackjack!\n\nPlease check the rules if you are not familiar with them -> '
          'http://hu.blackjack.org/blackjack-szabalyok/\n')


def total_money():
    print(f"New turn!\n__________________\nYou have {player_chip} money!")


def hit():
    global player, deck, end
    # time.sleep(2)
    player.add_card(deck.deal())
    player.calc_value()
    if not busted(player):
        show_hand()
        player_input()
    else:
        dealer.show()
        show_hand()
        time.sleep(1.5)
        clear()
        print('You are Busted!\n')
        end = True
        player_input()


def busted(who):
    global end
    if who.calc_value() > 21:
        end = True
        return True
    else:
        return False


def stand():
    global dealer, deck, end
    dealer.show()
    show_hand()
    time.sleep(2)
    while dealer.calc_value() < 17:
        dealer.add_card(deck.deal())
        show_hand()
        time.sleep(2)
        if busted(dealer):
            clear()
            print('Dealer Busted!\n')
            time.sleep(1.5)
            break
    end = True
    end_turn()


def show_hand():
    clear()
    global player, dealer
    print('__________________')
    print(f'Your {player}')
    print('__________________')
    print(f"Dealer's {dealer}\n")


def win():
    clear()
    global pool, player_chip
    print(f'Player win {pool * 2}!\n')
    player_chip += pool * 2
    pool = 0


def lose():
    clear()
    global pool
    print(f'Dealer won! Better Luck next time!\n')
    pool = 0


def draw():
    clear()
    global pool, player_chip
    print('Draw!\n')
    player_chip += pool
    pool = 0


def place_bet():
    global player_chip, pool
    bet = int(input('Please place your bet!: '))
    if player_chip >= bet > 0:
        player_chip -= bet
        pool += bet
    elif bet <= 0:
        print("You can't bet negative or zero. Please add a Valid value!")
        place_bet()
    else:
        # use exception
        print("Please add a number!")
        place_bet()


def has_blackjack(hand):
    if hand.value == 21 and hand.ace and len(player.cards) == 2:
        return True
    else:
        return False


def player_input():
    if not end:
        choice = str(input("Enter 'h' for hit, 's' for stand!: "))
        if choice.lower().startswith('h'):
            hit()
        elif choice.lower().startswith('s'):
            stand()
        else:
            print('Please add a Valid value!')
            player_input()
    else:
        choice = str(input("Do you want to quit?\nEnter (y/n): "))
        if choice.lower().startswith('y'):
            print('Thank you for participating!')
            quit()
        elif choice.lower().startswith('n'):
            clear()
            game()
        else:
            print('Please add a Valid value!')
            player_input()


def game():
    global player, dealer, deck, end
    end = False
    while not end:
        total_money()
        place_bet()

        player = Hand()
        # show whole hand of the player
        player.show()

        dealer = Hand()
        # initial deal for Player - 2 cards
        player.add_card(deck.deal())
        player.add_card(deck.deal())
        # initial deal for Dealer - 2 cards
        dealer.add_card(deck.deal())
        dealer.add_card(deck.deal())

        show_hand()
        if has_blackjack(player):
            win()
        player_input()


def end_turn():
    global player, dealer, pool, player_chip
    if busted(player):
        lose()
    elif busted(dealer):
        win()
    elif player.calc_value() > dealer.calc_value():
        win()
    elif player.calc_value() == dealer.calc_value():
        draw()
    else:
        lose()
    if player_chip == 0:
        print("You have no more money! Game Over!")
        quit()
    player_input()


def initial_setup():
    global player, dealer, deck
    deck = Deck()
    print('Shuffling Deck...')
    time.sleep(2)
    deck.shuffle_deck()
    print('Shuffling done...\n')
    time.sleep(1)


def blackjack():
    welcome()
    initial_setup()
    game()


# main function
if __name__ == "__main__":
    blackjack()
