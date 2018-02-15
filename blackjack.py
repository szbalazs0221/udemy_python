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

dealer = None
player = None
deck = None

player_chip = 100
pool = 0
leave = False
end_turn = False


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
            return f'Hand: {current_hand}\nValue: {self.calc_value()}'
        # Need to handle if Ace value turns to 10, hidden showing calculates with 1
        else:
            current_hand = self.cards[0].__str__() + ' ??'
            return f'Hand: {current_hand}\nValue: {self.calc_value()-values[self.cards[1].rank]}'


# Other methods
def welcome():
    print('Hello, welcome to Blackjack!\n\nPlease check the rules if you are not familiar with them -> '
          'http://hu.blackjack.org/blackjack-szabalyok/\n')


def total_money():
    print(f"You have {player_chip} money!")


def create_decks():
    pass


def game_step():
    pass


def hit():
    global player, deck
    player.add_card(deck.deal())
    player.calc_value()
    if player.value < 21:
        show_hand(dealer.hidden)
        player_input()
    elif player.value > 21:
        print('Busted!')


def busted():
    pass


def stand():
    global dealer, deck
    dealer.show()
    show_hand()
    while dealer.calc_value <= 17:
        dealer.add_card(deck.deal())
        show_hand()
    evaluate_round()


def show_hand():
    global player, dealer
    print(f'Your {player}')
    print(f'Dealer {dealer}')


def evaluate_round():
    global player, dealer, pool, player_chip
    if player.calc_value() > dealer.calc_value():
        player_chip += pool * 2
        print(f'Player win {pool * 2}!')
        pool = 0


def place_bet():
    global player_chip, pool
    bet = int(input('Please place your bet!: '))
    if player_chip == 0:
        print("You have no more money! Game Over!")
        quit()
    elif player_chip >= bet > 0:
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
    global leave
    choice = str(input("Enter 'h' for hit, 's' for stand, 'q' for quit!: "))
    if choice.lower().startswith('h'):
        hit()
    elif choice.lower().startswith('s'):
        stand()
    elif choice.lower().startswith('q'):
        print('Thank you for participating!')
        quit()
        leave = True
    else:
        print('Please add a Valid value!')
        player_input()


def start_turn():
    global player, dealer, deck
    while not leave:
        total_money()
        place_bet()

        player = Hand()
        player.show()

        dealer = Hand()

        player.add_card(deck.deal())
        player.add_card(deck.deal())

        dealer.add_card(deck.deal())
        dealer.add_card(deck.deal())

        show_hand()
        if has_blackjack(player):
            break
        player_input()


def initial_setup():
    global player, dealer, deck
    deck = Deck()
    print('Shuffling Deck...')
    deck.shuffle_deck()
    print('Shuffling done...\n')


def blackjack():
    welcome()
    initial_setup()
    start_turn()


# main function
if __name__ == "__main__":
    blackjack()
