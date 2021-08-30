import random

## Jeff Han
## Deck of Cards Challenge
## Appian
## Aug. 30, 2021

Value = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
Suit= ["Hearts", "Spades", "Clubs", "Diamonds"]

class Card:
    # Card is going to take a suit and value self.
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # This method will print out the value and suit of each card.
    def show(self):
        print(self.value, "of" ,self.suit)

class Deck:
    # Initalize with an empty list which will append to and a build method to create the deck.
    def __init__(self):
        self.cards= []
        self.__build()

        # Used for test method; this number can be changed accordingly for testing.
        self.max_size = 52

    # Build method takes in a for loop that will loop through 4 suits and 
    # another for loop to loop through 13 values for all 52 cards.
    def __build(self):
        for suit in Suit:
            for value in Value:
                self.cards.append(Card(suit, value))

    # This method takes in self for every card in the list and display the card.
    def show(self):
        for c in self.cards:
            c.show()
    
    # Shows the current count of cards in a deck.
    def count(self):
        return print("Remaining Cards in the Deck:", len(self.cards))
    
    # Shuffles the cards in the deck using the Fisher-Yates shuffle and not the
    # library-provided "shuffle".
    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    # This function will deal a card to the caller. If the deck is empty,
    # then no cards are dealt.
    def dealOneCard(self):
        if self.cards == []:
            print ("Empty deck, no cards are dealt.")
        else:
            return self.cards.pop()
    
    # A test function to verify cards are not dealt on/after the 53rd call
    # using the dealOneCard() and show() method. Also uses count() to keep
    # track of the remaining cards.
    def test(self):
        for i in range(self.max_size):
            try:
                self.dealOneCard().show()
                self.count()
            except:
                pass

# Main function is to show all the cards in order of the default deck with 
# the counts. Subsequently, the function will shuffle the cards using shuffle() 
# while displaying the respective counts to ensure no cards are lost during
# the shuffle. Next, the dealer will deal 52 card to the caller using test().
# Finally, the caller will ask for a 53rd using dealOneCard() and no card 
# will be dealt.
def main():
    deck = Deck()
    deck.show()
    deck.count()
    deck.shuffle()
    deck.show()
    deck.count()
    deck.test()
    deck.dealOneCard()
if __name__=="__main__":
    main()